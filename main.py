# Kivy's install_twisted_rector MUST be called early on!
from kivy.support import install_twisted_reactor
install_twisted_reactor()

from kivy.app import App
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

from autobahn.twisted.wamp import ApplicationSession
from autobahn.twisted.wamp import ApplicationRunner

from twisted.internet.defer import inlineCallbacks


class WampComponent(ApplicationSession):
    """
    A WAMP app component run from the Kivy UI.
    """

    def onJoin(self, details):
        # print("session ready", self.config.extra)

        # get the Kivy UI component this session was started from
        ui = self.config.extra['ui']
        ui.on_session(self)

        # subscribe to WAMP PubSub event and call the Kivy UI component when
        # events are received
        self.subscribe(ui.on_vote_message, u'io.crossbar.demo.vote.onvote')
        self.subscribe(ui.on_reset_message, u'io.crossbar.demo.vote.onreset')


class MilkshakeRoot(BoxLayout):
    milkshakes = ObjectProperty(None)
    milkshake_dict = {}

    def add_milkshake(self, name):
        milkshake = Factory.MilkshakeWidget()
        milkshake.name = name
        self.milkshakes.add_widget(milkshake)
        self.milkshake_dict[name] = self.milkshakes.children[0]

    @inlineCallbacks
    def on_session(self, session):
        """
        Called from WAMP session when attached to router.
        """
        self.session = session

        votes = yield self.session.call(u'io.crossbar.demo.vote.get')
        for vote in votes:
            self.milkshake_dict[vote[u'subject']].amount = vote[u'votes']

    def send_vote(self, subject):
        if self.session:
            self.session.call(u'io.crossbar.demo.vote.vote', subject)

    def send_reset(self):
        if self.session:
            self.session.call(u'io.crossbar.demo.vote.reset')

    def on_vote_message(self, msg):
        """
        Called from WampComponent when message was received in a PubSub event.
        """
        self.milkshake_dict[msg[u'subject']].amount = msg[u'votes']

    def on_reset_message(self):
        """
        Called from WampComponent when message was received in a PubSub event.
        """
        for milkshake in self.milkshakes.children:
            milkshake.amount = 0


class MilkshakeManiaApp(App):

    def build(self):

        self.root = MilkshakeRoot()
        milkshake_names = [u'Banana', u'Chocolate', u'Lemon']
        for milkshake_name in milkshake_names:
            self.root.add_milkshake(milkshake_name)

        # WAMP session
        self.session = None

        # run our WAMP application component
        # runner = ApplicationRunner(url=u"wss://demo.crossbar.io/ws",
        #  realm=u"crossbardemo", extra=dict(ui=self.root))
        runner = ApplicationRunner(url=u'ws://127.0.0.1:8080/ws',
                                   realm=u'realm1',
                                   extra=dict(ui=self.root))
        runner.run(WampComponent, start_reactor=False)

        return self.root


if __name__ == '__main__':
    MilkshakeManiaApp().run()

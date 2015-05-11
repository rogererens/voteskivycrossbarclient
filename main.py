from kivy.app import App
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout


class MilkshakeRoot(BoxLayout):
    milkshakes = ObjectProperty(None)

    def add_milkshake(self, name):
        milkshake = Factory.MilkshakeWidget()
        milkshake.name = name
        self.milkshakes.add_widget(milkshake)

    def reset_numbers(self):
        for milkshake in self.milkshakes.children:
            milkshake.number_ordered = 0


class MilkshakeWidget(BoxLayout):

    def increase_number(self):
        self.number_ordered += 1


class MilkshakeManiaApp(App):

    def build(self):
        root = MilkshakeRoot()
        milkshake_names = ['banana', 'chocolate', 'lemon']
        for milkshake_name in milkshake_names:
            root.add_milkshake(milkshake_name)
        return root


if __name__ == '__main__':
    MilkshakeManiaApp().run()

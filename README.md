# Writing Kivy apps using Autobahn|Python

This example shows how to use WAMP in a [Kivy](http://kivy.org/) app by
means of Autobahn|Python.

## Installing Kivy

### MS Windows ###

See the Crossbar/Kivy example.

### Mac OS X ###

Download the .dmg file from [Kivy's download page](http://kivy.org/#download) and follow the 
[instructions](http://kivy.org/docs/installation/installation-macosx.html#).
You can safely skip the [section with instructions to install the developer's version]
(http://kivy.org/docs/installation/installation-macosx.html#installing-the-dev-version)

Then use the python interpreter in the Kivy.app to install crossbar (which will install Autobahn|Python
as well) within the virtualenv that the Kivy.app is using:

```
kivy -m pip install crossbar
```

## Using a localhost based router and back-end

Go to your crossbarexamples/votes/python folder and start the Crossbar router:

```
crossbar start
```

which will start up a python back-end Votes component as well.

A Votes back-end component is needed: in case there would not be any front-end Votes
component running at all, the number of votes cast should still be kept.

## Using a Tavendo based router and back-end

Tavendo has got a Crossbar router and Votes back-end component running already.

## Starting a browser based front-end Votes component

Visit either file:///crossbarexamples/votes/python/web/index.html if you are using a localhost based router,
or open your Web browser at `https://demo.crossbar.io/demo/votes/web:8080` if you use Tavendo's router.

This will open a javascript based Votes front-end component in your web browser.

## Starting the example client

Finally! Go to the folder that contains this README.md file. If you are using a Mac, enter the command

```
kivy main.py
```

other platforms should use

```
python main.py
```

where python is the python interpreter used by Kivy.

This will start a Kivy based UI which incorporates a Votes front-end component.

You now can send message between the browser and Kivy UI:

![screenshot1.png](screenshot1.png)

#### Note
There may be other people be using a Votes front-end component using the same public
Crossbar.io server, so expect unexpected number of votes!


### Roadmap

- In the Google Play store you can obtain this Kivy demo at ...
- In the Apple Play store it is available as well ...
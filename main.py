from kivy.app import App
from kivy.uix.label import Label

class Main(App):
    def build(self):
        widget = Label()
        widget.text = 'Hello world!'
        widget.font_size = 50
        widget.color = 0,1,0,1

        return widget

Main().run()
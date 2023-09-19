#import kivy class
from kivy.app import App
from kivy.uix.label import Label

#define class to add widgets to it
class Main(App):
    #build function adds widgets and other components to the screen
    def build(self):
        #define the Label class and change its values (font_size, color)
        widget = Label()
        widget.text = 'Hello world!'
        widget.font_size = 50
        widget.color = 0,1,0,1
        
        return widget

Main().run()

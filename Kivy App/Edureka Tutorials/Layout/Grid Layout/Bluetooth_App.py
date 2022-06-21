
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class Grid_Layout_Demo(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 3
        self.cols = 1

        self.l1 = Label(
            text = "Bluetooth App"
        )
        self.add_widget(self.l1)

        self.on = Button(
            text = "ON",
            background_color = (0,255,67,1),
            color = (0,0,0,1)
        )
        self.bttn.bind(on_press = self.call_back_ON)
        self.add_widget(self.on)

        self.off = Button(
            text = "OFF",
            background_color = (25,2,200,1),
            color = (0,0,0,1)
        )
        self.bttn.bind(on_press = self.call_back_OFF)
        self.add_widget(self.off)

    def call_back_ON(self, elem):
        self.pop.content.text = self.txt.text
        self.pop.open()

    def call_back_OFF(self, elem):
        self.pop.content.text = self.txt.text
        self.pop.open()

class DemoApp(App):
    def build(self):
        return Grid_Layout_Demo()

demo = DemoApp()
demo.run()

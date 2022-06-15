
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class Grid_Layout_Demo(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 2
        self.cols = 1

        self.l1 = Label(
            text = "Pls click the button"
        )
        self.add_widget(self.l1)

        self.b1 = Button(
            text = "Click me",
            background_color = (0,24,67,1),
            color = (0,0,0,1)
        )
        self.add_widget(self.b1)

class DemoApp(App):
    def build(self):
        return Grid_Layout_Demo()

demo = DemoApp()
demo.run()

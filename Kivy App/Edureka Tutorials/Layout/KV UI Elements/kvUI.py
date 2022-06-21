
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.image import Image

class Kivy_UI(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.rows = 4

        self.img = Image(
            source = 'bulbon.jpg'
        )
        self.add_widget(self.img)

        self.lab = Label(
            text = "Enter Your Name"
        )
        self.add_widget(self.lab)

        self.txt = TextInput(
            text = "",
            font_size = 40
        )
        self.add_widget(self.txt)

        self.bttn = Button(
            text = "Submit"
        )
        self.bttn.bind(on_press = self.call_back)
        self.add_widget(self.bttn)

        self.pop = Popup(
            title = "Pop-Up Display",
            size = (400, 400),
            content = Label(
                text = ""
            )
        )

    def call_back(self, elem):
        self.pop.content.text = self.txt.text
        self.pop.open()

class DemoApp(App):
    def build(self):
        return Kivy_UI()

demo = DemoApp()
demo.run()

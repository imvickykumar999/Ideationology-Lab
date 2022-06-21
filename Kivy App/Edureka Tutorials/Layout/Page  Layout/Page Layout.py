from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.uix.button import Button

class Page_layout_Demo(PageLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.bttn1 = Button(
            text = "Button 1",
        )
        self.add_widget(self.bttn1)

        self.bttn2 = Button(
            text = "Button 2",
        )
        self.add_widget(self.bttn2)

class DemoApp(App):
    def build(self):
        return Page_layout_Demo()

demo = DemoApp()
demo.run()

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup

x = 'Connected'
try:
    import socket
    serverMACAddress = '00:20:10:08:1D:DA'  # Put your HC-05 address here
    port = 1  # Match the setting on the HC-05 module

    s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    s.connect((serverMACAddress,port))
except Exception as e:
    x = 'Could Not Connect'

class Grid_Layout_Demo(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 3
        self.cols = 1

        self.l1 = Label(
            text = "Bluetooth App : " + str(x)
        )
        self.add_widget(self.l1)

        self.on = Button(
            text = "ON",
            background_color = (0,255,67,1),
            color = (0,0,0,1)
        )
        self.on.bind(on_press = self.call_back_ON)
        self.add_widget(self.on)

        self.off = Button(
            text = "OFF",
            background_color = (25,2,200,1),
            color = (0,0,0,1)
        )
        self.off.bind(on_press = self.call_back_OFF)
        self.add_widget(self.off)

        self.pop = Popup(
            title = "Pop-Up Display",
            size = (400, 400),
            content = Label(
                text = ""
            )
        )

    def call_back_ON(self, elem):
        try:
            s.send(bytes('11111', 'UTF-8'))
        except:
            self.pop.content.text = "First Connect to Bluetooth"
            self.pop.open()

    def call_back_OFF(self, elem):
        try:
            s.send(bytes('00000', 'UTF-8'))
        except:
            self.pop.content.text = "First Connect to Bluetooth"
            self.pop.open()

class DemoApp(App):
    def build(self):
        return Grid_Layout_Demo()

demo = DemoApp()
demo.run()
s.close()

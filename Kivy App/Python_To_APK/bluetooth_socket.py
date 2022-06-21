
import socket
serverMACAddress = '00:20:10:08:1D:DA'  # Put your HC-05 address here
port = 1  # Match the setting on the HC-05 module

s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((serverMACAddress,port))
print("Connected. Type something...")

while 1:
    text = input()
    if text == "quit":
        break
    s.send(bytes(text, 'UTF-8'))
s.close()

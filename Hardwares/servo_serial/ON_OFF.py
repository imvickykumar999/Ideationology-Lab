
# pip3 install --upgrade pyserial
import serial                                 # add Serial library for Serial communication

Arduino_Serial = serial.Serial('com8', 9600)  #Create Serial port object called arduinoSerialData
print (Arduino_Serial.readline())               #read the serial data and print it as line
print ("Enter 1 to ON and 0 to OFF LED and servo")

while 1:                                      #infinite loop
    input_data = input()                  #waits until user enters data
    print ("you entered", input_data)           #prints the data for confirmation
    
    if (input_data == '1'):                   #if the entered data is 1 
        Arduino_Serial.write(b'1')             #send 1 to arduino
        print ("Servo at 90 and LED ON")
       
    if (input_data == '0'):                   #if the entered data is 0
        Arduino_Serial.write(b'0')             #send 0 to arduino 
        print ("Servo at 0 and LED OFF")
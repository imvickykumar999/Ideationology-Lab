
# https://stackoverflow.com/a/55545493/11493297

import serial, keyboard
import cv2
import numpy as np
from datetime import datetime as d

width = 1000
height = 1000

# Make empty black image of size (100,100)
img = np.zeros((height, width, 3), np.uint8)

white = [255,255,255]
filename = 'traced.jpg'

serialport = serial.Serial('COM8', baudrate=9600, timeout=2)
textfile = open('exported.csv', 'w')

while True:
    arduinodata = serialport.readline().decode('ascii')
    comma_sep = arduinodata.split(',')

    trace = int(comma_sep[0]) +512, int(comma_sep[1]) +512
    date = d.now()
    col = date.strftime("%Y-%m-%d   %H:%M:%S:%f,")
    
    print(trace, col)
    textfile.write(col + arduinodata)

    # Change pixel (50,50) to white
    # img[50,50] = white
    cv2.circle(img, (trace), 10, white, -1)

    # cv2.imshow('img', img)
    cv2.imwrite(filename, img)
    cv2.waitKey(0)

    if keyboard.is_pressed('q'):  # if key 'q' is pressed 
        break  # finishing the loop

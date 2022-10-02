
from machine import Pin
import utime

p2 = Pin(25, Pin.OUT)

while(True):
    p2.value(0)
    print("off")
    utime.sleep(1)  
    p2.value(1)
    print("on")
    utime.sleep(1)
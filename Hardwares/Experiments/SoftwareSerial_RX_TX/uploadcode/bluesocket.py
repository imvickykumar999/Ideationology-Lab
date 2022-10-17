    
import psutil, time, socket

# serverMACAddress = 'FC:A8:9A:00:21:16'  # Put your HC-05 address here
serverMACAddress = '00:21:09:00:55:71'  # Put your HC-05 address here
port = 1                                # Match the setting on the HC-05 module

s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((serverMACAddress,port))

i = 0
battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

# maxbat = 97
# minbat = 30
# print(percent)

maxbat = percent+1
minbat = percent-1

if plugged == False:
    plugged = "Not Plugged In"
else:
    plugged = "Plugged In"

status = str(percent) + '% | ' + plugged
print(status)

count = 0
data = []
while True:

    battery = psutil.sensors_battery()
    pluggedbool = battery.power_plugged
    percent = battery.percent
    
    if pluggedbool == False:
        plugged = "Not Plugged In"
    else:
        plugged = "Plugged In"
        
    count += 1
    i += 1
    data.append(percent)

    print(str(count), '). ', str(percent), '[', str(maxbat), str(minbat), ']', plugged, str(battery))
    time.sleep(3)

    if percent >= maxbat:
        text = '0000000000000000000'
        s.send(bytes(text, 'UTF-8'))

        # print("\nWaiting for 60 seconds...\n")
        # time.sleep(60)
        continue

    if percent <= minbat:
        text = '11111111111111111111'
        s.send(bytes(text, 'UTF-8'))

        # print("\nWaiting for 60 seconds...\n")
        # time.sleep(60)
        continue

    else:
        continue

s.close()
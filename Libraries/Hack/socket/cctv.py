
# https://reolink.com/ip-camera-address/
# url = 'https://my.ivideon.com/cameras/groups/own'

ipad = '''rmnet0: 10.36.247.89
swlan0: 192.168.230.81
rmnet1: 10.169.151.247'''

import cv2

# aud = 'http://192.168.109.171:8080/audio.wav'
vid = 'http://192.168.230.81:8080/video'
# cmd = 'start microsoft.windows.camera:'

# cap = cv2.VideoCapture('rtsp://admin1:password@192.168.0.253/out.h264')
cap = cv2.VideoCapture(vid)
# cap = cv2.VideoCapture('output.mp4')
# cap = cv2.VideoCapture(0) # 1 for back camera, 0 for front.

while True:
    ret, frame = cap.read()
    cv2.imshow("Capturing",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
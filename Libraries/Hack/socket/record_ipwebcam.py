import cv2
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

freq = 44100
duration = 6

recording = sd.rec(int(duration * freq),
                samplerate=freq, channels=2)

afile = 'output.mp3'
vfile = 'output.mp4'
sd.wait()

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
# url = 'https://my.ivideon.com/cameras/groups/own'
# aud = 'http://192.168.109.171:8080/audio.wav'
# vid = 'http://192.168.109.171:8080/video'

# cap = cv2.VideoCapture('rtsp://admin:123456@192.168.1.216/H264?ch=1&subtype=0')
# cap = cv2.VideoCapture(vid)
cap = cv2.VideoCapture(0)

cap.set(3,640)
cap.set(4,480)

fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter(vfile, fourcc, 20.0, (640,480))

while(True):
    ret, frame = cap.read()
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5) 

    for x,y,w,h in faces:
        frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3) 

    out.write(frame)
    wv.write(afile, recording, freq, sampwidth=2)

    cv2.imshow('frame', frame)
    c = cv2.waitKey(1)
    
    if c & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

import os
os.startfile(afile)
os.startfile(vfile)
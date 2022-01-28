# !pip install bs4

from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import numpy as np

user1 = 'imvickykumar999'
user2 = 'ayu4tor'

def fetch_data(user):
    gurl = f'https://github.com/{user}'
    r = requests.get(gurl)
    soup = BeautifulSoup(r.content, 'html5lib')

    a = soup.findAll('rect', attrs = {'class':'ContributionCalendar-day'})
    x = []
    y = []

    for i in a:
        try:
            x.append(i['data-date'])
            y.append(int(i['data-count']))
        except:
            pass

    x1 = x[::-1][:30][::-1]
    y1 = y[::-1][:30][::-1]

    xpoints = np.array(x1)
    ypoints = np.array(y1)
    return xpoints, ypoints

fig = plt.figure(figsize=(10,3))
plt.xticks(rotation=90)
plt.grid()

plt.plot(fetch_data(user1)[0], fetch_data(user1)[1], label=user1)
plt.plot(fetch_data(user2)[0], fetch_data(user2)[1], label=user2)

plt.legend()
# plt.show()
fig.savefig(f'user/{user1}+{user2}.jpg')

from PIL import Image

def make_square(im, min_size=256, fill_color=(255,255,255,0)):
    x, y = im.size
    size = max(min_size, x, y)
    new_im = Image.new('RGB', (size, size), fill_color)
    new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
    return new_im

test_image = Image.open(f'user/{user1}+{user2}.jpg')
new_image = make_square(test_image)
new_image.save(f'user/{user1}+{user2}+squared.jpg')

from instabot import Bot
import getpass
bot = Bot()

def upload(user, passwd, path, cap):
    bot.login(username = user, password = passwd)
    up = bot.upload_photo(path, caption = cap)
    return up

user = '_____.___alone___._____'
passwd = getpass.getpass('Enter Password : ')

path = f'user/{user1}+{user2}+squared.jpg'
cap = '🔥This image is uploaded using python code✨'

upload(user, passwd, path, cap)

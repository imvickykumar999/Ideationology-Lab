# !pip install bs4

from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import numpy as np

user1 = 'imvickykumar999'
user2 = 'CSSEGISandData'
# user3 = 'ayu4tor'

def fetch_data(user):
    gurl = f'https://github.com/{user}'

    r = requests.get(gurl)
    soup = BeautifulSoup(r.content, 'html5lib')

    a = soup.findAll('rect', attrs = {'class':'ContributionCalendar-day'})
    x = []
    y = []

    for i in a:
        try:
            dt = i['data-date'].split('-')[-1]
            x.append(dt)
            y.append(int(i['data-count']))
        except:
            pass
    
    longest = 0
    streak = 0
    mylist = y[::-1]

    for elem in mylist:
        if elem != 0:
            streak += 1
        else:
            longest = max(longest, streak)
            break

    x1 = x[::-1][:30][::-1]
    y1 = y[::-1][:30][::-1]

    xpoints = np.array(x1)
    ypoints = np.array(y1)

    return (xpoints, ypoints,
         f"{user}'s Streaks is {max(longest, streak)} days")

fig = plt.figure(figsize=(10,3))
# plt.xticks(rotation=90)
plt.grid()

fdu1 = fetch_data(user1)
fdu2 = fetch_data(user2)
# fdu3 = fetch_data(user3)

plt.plot(fdu1[0], fdu1[1], label=fdu1[2])
plt.plot(fdu2[0], fdu2[1], label=fdu2[2])
# plt.plot(fdu3[0], fdu3[1], label=fdu3[2])

plt.legend()
fig.suptitle('(x-axis) Last 30 Days Git Commits', fontsize=15)

# plt.xlabel('Date', fontsize=15)
plt.ylabel('No. of Commits', fontsize=12)
# plt.show()

pth = f'{user1}+{user2}.jpg'
fig.savefig(pth)

from PIL import Image

def make_square(im, min_size=256, fill_color=(255,255,255,0)):
    x, y = im.size
    size = max(min_size, x, y)
    new_im = Image.new('RGB', (size, size), fill_color)
    new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
    return new_im

test_image = Image.open(pth)
new_image = make_square(test_image)
new_image.save(pth)

# from instabot import Bot
# import getpass
# bot = Bot()

# def upload(user, passwd, path, cap):
#     bot.login(username = user, password = passwd)
#     up = bot.upload_photo(path, caption = cap)
#     return up

# user = '_____.___alone___._____'
# passwd = getpass.getpass('Enter Password : ')

# cap = f'{pth} is uploaded using python code ✨'
# upload(user, passwd, pth, cap)

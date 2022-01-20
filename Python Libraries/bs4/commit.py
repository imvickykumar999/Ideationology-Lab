from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import numpy as np
import sys

# user = 'imvickykumar999'
# month = 2

try:
    user = sys.argv[1]
    month = int(sys.argv[2])
    gurl = f'https://github.com/{user}'

    r = requests.get(gurl)
    soup = BeautifulSoup(r.content, 'html5lib')

    a = soup.findAll('rect', attrs = {'class':'ContributionCalendar-day'})
    x, y = [], []

    for i in a:
        try:
            c = int(i['data-count'])
            d = i['data-date']
            y.append(c)
            x.append(d)
        except:
            pass

    x = x[::-1][:30*month][::-1]
    y = y[::-1][:30*month][::-1]
    fig = plt.figure(figsize=(10*month,3*month))

    xpoints = np.array(x)
    ypoints = np.array(y)
    plt.xticks(rotation=90)

    plt.title(f'GitHub username : {user}')
    plt.xlabel(f"Date (of last {month} month(s))")
    plt.ylabel("Git Commit")

    plt.plot(xpoints, ypoints)
    # plt.show()
    fig.savefig(f'user/{user}.png')
    print('Graph saved')

except Exception as e:
    print(e)

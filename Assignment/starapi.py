from bs4 import BeautifulSoup
import requests

def stars(user = 'imvickykumar999', repo = 'imvickykumar999'):
    url = f'https://github.com/{user}/{repo}'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    try:
        a = soup.findAll('a', attrs = {'href': f'/{user}/{repo}/stargazers'})
        txt = a[1].strong.text
    except:
        txt = '0'

    d = {'Repository' : repo,
    'Stars' : txt,
    }
    print(user, d)
    return d

def followers(user = 'imvickykumar999'):
    try:
        url = f'https://github.com/{user}?tab=followers'
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')
        a = soup.findAll('span', attrs = {'class': 'Link--secondary'})

        follow = []
        for i in a:
            follow.append(i.text.strip())
        return follow
    except:
        return

def star_api(user = 'imvickykumar999'):
    try:
        url = f'https://github.com/{user}?tab=repositories'
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')
        a = soup.findAll('div', attrs = {'class': 'd-inline-block mb-1'})

        up=[]
        for i in a:
            repo = i.h3.a.text.strip()
            up.append(stars(user, repo))
        return up
    except:
        return

def my_api(user = 'imvickykumar999'):
    try:
        lst_followers = followers(user)
        lst_followers.insert(0, user)

        full_api = {}
        for i in lst_followers:
            full_api.update({i : star_api(i)})

        import json, os
        jfile = f'{user}.json'

        with open(jfile, 'w') as outfile:
            json.dump(full_api, outfile)

        os.startfile(jfile)
        return full_api
    except:
        return

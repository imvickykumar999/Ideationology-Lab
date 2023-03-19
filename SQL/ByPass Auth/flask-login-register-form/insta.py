"""View Instagram user follower count from Instagram public api"""
import requests

def getfollowedby(url):
    """View Instagram user follower count"""
    link = f'https://www.instagram.com/{url}/?__a=1&__d=1'
    user = requests.get(link)

    a = user.json()
    print(a)
    b = a['graphql']['user']['edge_followed_by']['count']
    
    c = a['graphql']['user']['edge_felix_video_timeline']['edges']
    d = a['graphql']['user']['edge_owner_to_timeline_media']['edges']
    return b, c+d

def getname(url):
    """Split the URL from the username"""
    sp = url.split("instagram.com/")
    rep = sp[0].replace("/", "")
    return rep


'''
a = user.json()
print(a)
# {'message': 'Please wait a few minutes before you try again.', 
'require_login': True, 'status': 'fail'}

Instagram doesn’t like bots because they distort the experience that users 
have on their platforms. While bots can be used for good purposes, 
such as providing customer support or delivering news updates, 
they can also be employed for nefarious reasons, like spreading 
misinformation or deliberately flooding a conversation with spam comments.
'''

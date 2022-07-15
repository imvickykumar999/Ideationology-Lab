
from bs4 import BeautifulSoup
import requests
 
username = "imvickykumar999"
 
github_html = requests.get(f'https://github.com/{username}').text
soup = BeautifulSoup(github_html, "html.parser")

avatar_block = soup.find_all('img',class_='avatar')
print(avatar_block[4]['src'])

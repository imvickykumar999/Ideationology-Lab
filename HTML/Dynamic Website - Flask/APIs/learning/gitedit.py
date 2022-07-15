import json
import requests
from getpass import getpass

# Login to GitHub and go to Settings > Developer settings > Personal access tokens and generate a new token. 
# For scope click the user checkmark and generate token. 
# Save it elsewhere as after you close the tab you will not be able to see it again on your profile.

api_token = getpass('API Token: ')
user = 'imvickykumar999'

h = {'Accept': 'application/vnd.github+json',
        'Authorization': 'token ' + api_token}

def main():
    get_bio("Old bio: ")
    new_bio = input("Enter new bio: ")
    bio_patch = requests.patch(f'https://api.github.com/users/{user}', json = {'bio': new_bio}, headers = h)
    print ("Status: ", bio_patch.status_code)
    get_bio("New bio: ")

def get_bio(context):
    r = requests.get(f'https://api.github.com/users/{user}', headers=h)
    json = r.json()
    print(json)
    
if __name__ == "__main__":
    main()

"""
A sample script for using an incoming webhook for Hangouts chat rooms.
"""

from json import dumps
from httplib2 import Http


def main(url):
    """Hangouts Chat incoming webhook quickstart."""
    url = url
    bot_message = {
        'text' : text,
          "cards": [
            {
              "sections": [
                {
                  "widgets": [
                    {
                      "textParagraph": {
                        "text": "<b>Roses</b> are <font color=\"#ff0000\">red</font>,<br><i>Violets</i> are <font color=\"#0000ff\">blue</font>"
                      }
                    }
                  ]
                }
              ]
            },
            {
          "sections": [
            {
              "widgets": [
                {
                  "image": {
                    "imageUrl": "https://developers.google.com/chat/images/cards-image.png",
                    "onClick": {
                      "openLink": {
                        "url": "https://developers.google.com/chat/api/guides/message-formats/cards#image_widget/"
                      }
                    }
                  }
                }
              ]
            }
          ]
        }
      ]
    }

    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}

    http_obj = Http()

    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )

    print(response)

if __name__ == '__main__':
    text = input('Write message : ')

    if text == '':
        text = '''
    Hey Vicks,
    Hello from a Python script!
    '''

    url1 = 'https://chat.googleapis.com/v1/spaces/AAAAOq_JWnk/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=0shxYWv8zlaNB9CVYeI5ayOKJhbyjqn562Cd5NmZXxU%3D'
    url2 = 'https://chat.googleapis.com/v1/spaces/AAAAe-ewe8U/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=08oGdB2rGkMAHPYXg3VmNWbLGG0jgLLAXwsl_F3Fsog%3D'
    url3 = 'https://chat.googleapis.com/v1/spaces/AAAAe-ewe8U/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=oHzjFlOMiHNYAVyceo9lZ21eoMRhSpIgV8fNM8AZB8M%3D'
    url4 = 'https://chat.googleapis.com/v1/spaces/AAAA-pCtR2s/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=qnVg1YsSs0sTBr8Bs9jCBVfvHL0aPzBqjA49xpmq8oA%3D'
    url5 = 'https://chat.googleapis.com/v1/spaces/AAAA-pCtR2s/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=8mgD7uBcYFeCiu-NnDqjjQNx1eVPGXfxbOzk_EoH72Q%3D'

    lst = [url1, url2, url3, url4, url5]
    url = input('Enter url_x number (1/2/3/4/5) : ')

    if url == '':
        url = lst[4]
    else:
        url = lst[int(url)-1]

    main(url)


"""
A sample script for using an incoming webhook for Hangouts chat rooms.
"""

from json import dumps
from httplib2 import Http


def main():
    """Hangouts Chat incoming webhook quickstart."""
    url = url2
    bot_message = {
        'text' : '''Hey Vicks,
        Hello from a Python script!
        Its my first chat bot
        '''}

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
    url1 = 'https://chat.googleapis.com/v1/spaces/AAAAOq_JWnk/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=0shxYWv8zlaNB9CVYeI5ayOKJhbyjqn562Cd5NmZXxU%3D'
    url2 = 'https://chat.googleapis.com/v1/spaces/AAAAe-ewe8U/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=08oGdB2rGkMAHPYXg3VmNWbLGG0jgLLAXwsl_F3Fsog%3D'
    main()

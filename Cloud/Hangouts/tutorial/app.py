# https://developers.google.com/chat/how-tos/bots-publish

#!/usr/bin/env python3
"""Example bot that returns a synchronous response."""

from flask import Flask, request, json
app = Flask(__name__)

@app.route('/', methods=['POST'])
def on_event():
  """Handles an event from Google Chat."""
  event = request.get_json('ideationology-lab-339220-e996ca767b19.json')
  if event['type'] == 'ADDED_TO_SPACE' and not event['space']['singleUserBotDm']:
    text = 'Thanks for adding me to "%s"!' % (event['space']['displayName'] if event['space']['displayName'] else 'this chat')
  elif event['type'] == 'MESSAGE':
    text = 'You said: `%s`' % event['message']['text']
  else:
    return
  return json.jsonify({'text': text})

if __name__ == '__main__':
  app.run(port=8080, debug=True)

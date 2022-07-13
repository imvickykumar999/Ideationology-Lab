
import requests

response = requests.get("http://randomfox.ca/floof")
fox = response.json()
print(fox['image'])

import webbrowser
webbrowser.open(fox['image'])

from firebase_admin import credentials

cred = credentials.Certificate('ideationology-4c639-firebase-adminsdk-5hfwu-5806b97f02.json')

url = 'https://ideationology-4c639-default-rtdb.asia-southeast1.firebasedatabase.app/'
path = {'databaseURL' : url}

import firebase_admin
firebase_admin.initialize_app(cred, path)

from firebase_admin import db
refv = db.reference('counter/views')

g = refv.get()
g = g + 1
refv.set(g)
print(g)

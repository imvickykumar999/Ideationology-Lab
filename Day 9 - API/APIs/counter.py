# !pip install firebase_admin

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('vickservice-36ac9-firebase-adminsdk-ifzxv-e4df0f384c.json')

# Initialize the app with a None auth variable, limiting the server's access
url = 'https://vickservice-36ac9-default-rtdb.asia-southeast1.firebasedatabase.app/'
path = {'databaseURL': url}

firebase_admin.initialize_app(cred, path)

refv = db.reference("counter/views")
refv.set(refv.get()+1)

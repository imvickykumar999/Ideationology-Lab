# !pip install firebase_admin

from firebase_admin import credentials

# Fetch the service account key JSON file contents
cred = credentials.Certificate('vickservice-36ac9-firebase-adminsdk-ifzxv-e4df0f384c.json')

# Initialize the app with a None auth variable, limiting the server's access
url = 'https://vickservice-36ac9-default-rtdb.asia-southeast1.firebasedatabase.app/'
path = {'databaseURL': url}

import firebase_admin
firebase_admin.initialize_app(cred, path)

from firebase_admin import db
refv = db.reference("counter/views")
refv.set(refv.get()+1)

print(refv.get())

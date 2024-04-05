from firebase_admin import credentials
from datetime import datetime

# Load Firebase credentials
cred = credentials.Certificate('ideationology-4c639-firebase-adminsdk-5hfwu-5806b97f02.json')

# Set Firebase database URL
url = 'https://ideationology-4c639-default-rtdb.asia-southeast1.firebasedatabase.app/'
path = {'databaseURL': url}

# Initialize Firebase Admin SDK
import firebase_admin
from firebase_admin import db

firebase_admin.initialize_app(cred, path)

# Reference to the database node
refv = db.reference('counter/views')

# Get current timestamp and format it
timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

# Read current view count
views_data = refv.get()

# If there's no existing data or it's not a dictionary, initialize to zero
if views_data is None or not isinstance(views_data, dict):
    views_data = {'count': 0, 'timestamps': {}}

# Increment view count
views_data['count'] += 1

# Ensure 'timestamps' key exists and is a dictionary
if 'timestamps' not in views_data or not isinstance(views_data['timestamps'], dict):
    views_data['timestamps'] = {}

# Add timestamp for the current view
views_data['timestamps'][timestamp] = views_data['count']

# Update database with new data
refv.set(views_data)

# Print the updated view count and timestamps
print("Total views:", views_data['count'])
print("Timestamps of views:")
for ts, count in views_data['timestamps'].items():
    print(ts, ": Count -", count)

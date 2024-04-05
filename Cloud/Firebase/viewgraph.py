from firebase_admin import credentials
from datetime import datetime
import matplotlib.pyplot as plt

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

# Read current view count
views_data = refv.get()

# If there's no existing data or it's not a dictionary, initialize to zero
if views_data is None or not isinstance(views_data, dict):
    views_data = {'timestamps': {}}

# Convert timestamps to datetime objects for plotting
timestamps = [datetime.strptime(ts, "%Y-%m-%d %H-%M-%S") for ts in views_data['timestamps'].keys()]
counts = list(views_data['timestamps'].values())

# Plotting the graph
plt.figure(figsize=(10, 6))
plt.plot(timestamps, counts, marker='o', linestyle='-')
plt.title('Views Over Time')
plt.xlabel('Timestamp')
plt.ylabel('View Count')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

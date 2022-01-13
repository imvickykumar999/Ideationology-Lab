
def run():
    from firebase_admin import credentials
    import firebase_admin

    cred = credentials.Certificate('ideationology-4c639-firebase-adminsdk-5hfwu-5806b97f02.json')
    url = 'https://ideationology-4c639-default-rtdb.asia-southeast1.firebasedatabase.app/'
    path = {'databaseURL' : url}

    if not firebase_admin._apps:
        default_app = firebase_admin.initialize_app(cred, path)

    from firebase_admin import db
    refv = db.reference('counter/views')

    g = refv.get()
    g = g + 1
    refv.set(g)
    return g, url

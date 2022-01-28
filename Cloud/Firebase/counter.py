
def fire():
    from firebase_admin import credentials
    cred = credentials.Certificate('ideationology-4c639-firebase-adminsdk-5hfwu-5806b97f02.json')

    url = 'https://ideationology-4c639-default-rtdb.asia-southeast1.firebasedatabase.app/'
    path = {'databaseURL' : url}

    import firebase_admin
    firebase_admin.initialize_app(cred, path)

    from firebase_admin import db
    refv = db.reference('book/price')

    d = {'book1' : 190, 'book2' : 250}
    refv.set(d)

    refv = db.reference('book')
    g = refv.get()

    print(g)
    return g

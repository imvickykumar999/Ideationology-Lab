"""Flask Login Example and instagram fallowing find"""

from flask import Flask, url_for, render_template, request, redirect, session, flash
from insta import getfollowedby, getname
import sqlite3


app = Flask(__name__)
conn = sqlite3.connect('test.db', 
            check_same_thread=False)

conn.execute('''
        CREATE TABLE IF NOT EXISTS ADMIN (
        USERNAME CHAR(50) PRIMARY KEY,
        PASSWORD CHAR(50) NOT NULL )
''')


@app.route('/', methods=['GET', 'POST'])
def home():
    """ Session control"""

    if not session.get('logged_in'):
        return render_template('index.html')
    else:
        if request.method == 'POST':
            name = getname(request.form['username'])

            if name == '':
                return render_template('index.html')
            data = getfollowedby(name)

            return render_template('index.html', 
                username=name, 
                session=session,
                data=data[0], 
                full_data=data[1], 
                )
        return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login Form"""

    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form['username']
        password = request.form['password']

        try:
            statement = f'''
                SELECT * FROM ADMIN WHERE USERNAME='{username}' AND PASSWORD='{password}'
            '''
            crsr = conn.execute(statement)

            if crsr.fetchone() is None:
                flash("Either Username or Password is wrong")
                return render_template('login.html')
            else:
                session['logged_in'] = True
                session['username'] = username
            return redirect(url_for('home'))
            
        except Exception as e:
            return flash(f"{e}") 


@app.route('/register/', methods=['GET', 'POST'])
def register():
    """Register Form"""

    if request.method == 'POST':
        username=request.form['username']
        password=request.form['password']

        if username == '' or password == '':
            flash("Fill the empty field")
            return render_template('register.html')
        
        try:
            statement = f'''
                INSERT INTO ADMIN (USERNAME,PASSWORD) VALUES ('{username}', '{password}')
            '''
            conn.execute(statement)
            conn.commit()
            
        except:
            flash("Username already exists.")  
            return render_template('register.html')

        return render_template('login.html')
    return render_template('register.html')


@app.route("/logout")
def logout():
    """Logout Form"""

    session['logged_in'] = False
    flash("You are successfuly Logged out") 
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.debug = True
    app.secret_key = "123"
    app.run(debug=True)

# import routes
from flask import Flask
import os 
from flask_sqlalchemy import SQLAlchemy 

def create_the_database(db):
    db.create_all()

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # no warning messages
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///info.db' # for using the sqlite database

db = SQLAlchemy(app)

# Create User Table
class User(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    phone = db.Column(db.Integer)
    email = db.Column(db.String(50))
    job = db.Column(db.String(50))

def insert_data(name, phone, email, job):
    new_user = User(name=name, phone=phone, email=email, job=job)
    db.session.add(new_user)
    db.session.commit()

def modify_data(the_id, col_name, user_input):
    the_user = User.query.filter_by(id=the_id).first()
    if col_name == 'name':
        the_user.name = user_input
    elif col_name == 'phone':
        the_user.phone = user_input 
    elif col_name == 'email':
        the_user.email = user_input 
    elif col_name == 'job':
        the_user.job = user_input 
    
    db.session.commit() 


def delete_data(the_id):
    the_user = User.query.filter_by(id=the_id).first()
    db.session.delete(the_user)
    db.session.commit()
    

def get_all_rows_from_table():
    users = User.query.all()
    return users 
    

# if database does not exist in the current directory, create it!
db_is_new = os.path.exists('info.db')
if db_is_new:
    create_the_database(db)

insert = insert_data('name', 'phone', 'email', 'job')
obj = User.query.filter_by(name='name').first()
get_all_rows = get_all_rows_from_table()
print(get_all_rows, obj.id)
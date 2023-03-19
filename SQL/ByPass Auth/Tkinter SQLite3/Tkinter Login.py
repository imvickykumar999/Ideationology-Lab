
# https://www.geeksforgeeks.org/create-mysql-database-login-page-in-python-using-tkinter/
# https://www.w3schools.com/python/python_mysql_getstarted.asp
# https://www.krazyprogrammer.com/2020/12/login-with-sqlite-in-python-tkinter.html

'''
Should I use SQLite or MySQL?

MySQL has a well-constructed user management system which can handle 
multiple users and grant various levels of permission. 
SQLite is suitable for smaller databases. 
As the database grows the memory requirement also gets larger while 
using SQLite. Performance optimization is harder when using SQLite.

SQLite is probably the most straightforward database to 
connect to with a Python application since you don't need 
to install any external Python SQL modules to do so.
'''	

from tkinter import *
import  sqlite3

conn=sqlite3.connect("student.db")
print("\n", "Database created successfully")

conn.execute("""
CREATE TABLE IF NOT EXISTS ADMIN (
USERNAME TEXT PRIMARY KEY, 
PASSWORD TEXT NOT NULL)
""")
print ("Table ADMIN created successfully")


conn.execute("INSERT OR IGNORE INTO ADMIN(USERNAME,PASSWORD) VALUES ('admin', 'admin789')");
conn.execute("INSERT OR IGNORE INTO ADMIN(USERNAME,PASSWORD) VALUES ('krazy', 'krazy789')");

conn.commit()
print ("Records inserted successfully")


cursor = conn.execute("SELECT * from ADMIN")
print("ID\tUSERNAME\tPASSWORD")
for row in cursor:
   print ("{}\t{}\t\t{}".format(row[0],row[1],row[2]))


def login():
    uname=username.get()
    pwd=password.get()

    if uname=='' or pwd=='':
        message.set("fill the empty field!!!")
    else:
      conn = sqlite3.connect('student.db')

      statement = f'''
      SELECT * from ADMIN where USERNAME='{uname}' and PASSWORD='{pwd}'
      '''

      cursor = conn.execute(statement)
      print(statement)

      if cursor.fetchone():
       message.set("Login success")
      else:
       message.set("Wrong username or password!!!")

def Loginform():
    global login_screen
    login_screen = Tk()

    login_screen.title("@imvickykumar999")
    login_screen.geometry("350x250")
    login_screen["bg"]="#1C2833"

    global  message
    global username
    global password

    username = StringVar()
    password = StringVar()
    message=StringVar()

    Label(login_screen, width="300", text="Login From", bg="#0E6655",fg="white",font=("Arial",12,"bold")).pack()
    Label(login_screen, text="Username * ",bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=20,y=43)
    Entry(login_screen, textvariable=username,bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=120,y=45)
    
    Label(login_screen, text="Password * ",bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=20,y=80)
    Entry(login_screen, textvariable=password ,show="*",bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=120,y=82)
    Label(login_screen, text="",textvariable=message,bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=95,y=120)
    
    Button(login_screen, text="Login", width=10, height=1, command=login, bg="#0E6655",fg="white",font=("Arial",12,"bold")).place(x=125,y=170)
    login_screen.mainloop()

Loginform()

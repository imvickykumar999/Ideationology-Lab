
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="vicks",
  password="Hellovix999@"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")


# C:\Users\Vicky\Desktop\Repository\Basics-of-Python\SQL\Python MySQL>python create_database.py
# Traceback (most recent call last):
#   File "C:\Users\Vicky\AppData\Local\Programs\Python\Python39\lib\site-packages\mysql\connector\connection_cext.py", line 236, in _open_connection
#     self._cmysql.connect(**cnx_kwargs)
# _mysql_connector.MySQLInterfaceError: Access denied for user 'vicks'@'localhost' (using password: YES)

# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
#   File "C:\Users\Vicky\Desktop\Repository\Basics-of-Python\SQL\Python MySQL\create_database.py", line 4, in <module>
#     mydb = mysql.connector.connect(
#   File "C:\Users\Vicky\AppData\Local\Programs\Python\Python39\lib\site-packages\mysql\connector\__init__.py", line 272, in connect
#     return CMySQLConnection(*args, **kwargs)
#   File "C:\Users\Vicky\AppData\Local\Programs\Python\Python39\lib\site-packages\mysql\connector\connection_cext.py", line 85, in __init__
#     self.connect(**kwargs)
#   File "C:\Users\Vicky\AppData\Local\Programs\Python\Python39\lib\site-packages\mysql\connector\abstracts.py", line 1014, in connect
#     self._open_connection()
#   File "C:\Users\Vicky\AppData\Local\Programs\Python\Python39\lib\site-packages\mysql\connector\connection_cext.py", line 241, in _open_connection
#     raise errors.get_mysql_exception(msg=exc.msg, errno=exc.errno,
# mysql.connector.errors.ProgrammingError: 1045 (28000): Access denied for user 'vicks'@'localhost' (using password: YES)

# C:\Users\Vicky\Desktop\Repository\Basics-of-Python\SQL\Python MySQL>
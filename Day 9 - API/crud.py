
# pip install imvickykumar999
# C:\Users\Vicky\anaconda3\Lib\site-packages\vicksbase
# https://stackoverflow.com/questions/1802971/nameerror-name-self-is-not-defined

import json
from datetime import datetime, timedelta
# import socket

# print("Your Computer Name is:" + hostname)
# print("Your Computer IP Address is:" + IPAddr)

class vicks:
    def __init__(self,
                password,
                name = 'Anonymous',
                link = 'https://chatting-c937e-default-rtdb.firebaseio.com/',
                ):

        try:
            self.link = link
            self.name = name
            self.password = password

            from vicksbase import firebase as f
            print(f)
            self.firebase_obj = f.FirebaseApplication(self.link, None)
            # print(self.pull(child = '/'))

        except Exception as e:
            print(e)
            print('try: pip install imvickykumar999')

    def show(self):
        return self.link, self.name

    def pull(self,
             child = None):

        if self.password == '@Hey_Vicks':
            dt = datetime.now()

            d = str(dt).split()[0]
            t = str(dt).split()[1].split('.')[0]

            if child == None:
                child = f'Group/Chat/{d}/{t}'

            result = self.firebase_obj.get(f'{child}', None)
            return result

        else:
            error = '\n...Wrong Credentials !!!\n'
            print(error)
            return error

    def push(self, data = None,
                   child = None):

        if self.password == '@Hey_Vicks':
            dt = datetime.now()
            dt += timedelta(hours = 5, minutes = 30)

            d = str(dt).split()[0]
            t = str(dt).split()[1].split('.')[0]

            print('################->', t)

            # hostname = socket.gethostname()
            # IPAddr = socket.gethostbyname(hostname)
            # ip = '-'.join(IPAddr.split('.'))

            if child == None:
                # child = f"Group/Chat/{d}/{t}&{str(hostname+'*'+ip)}@{self.name}"
                child = f"Group/Chat/{d}/{t}/{self.name}"

            if data == None:
                data = f"...hi, I am {self.name}"

            self.firebase_obj.put('/', child, data)
            # self.firebase_obj.post(child, data)
            # return self.pull(child = '/')

        else:
            error = '\n...Wrong Credentials !!!\n'
            print(error)
            return error

    def add(self, data = None,
                   child = None):

        if self.password == '@Hey_Vicks':
            self.firebase_obj.post(child, data)

        else:
            error = '\n...Wrong Credentials !!!\n'
            print(error)
            return error

    def remove(self, child = 'A/B/C/led2'): # danger to run... loss of data.

        if self.password == '@Hey_Vicks':
            data = self.firebase_obj.delete('/', child)
            # return self.pull(child = '/')

        else:
            error = '\n...Wrong Credentials !!!\n'
            print(error)
            return error

    def save(self,
             child = None):

        if self.password == '@Hey_Vicks':
            dt = datetime.now()
            d = str(dt).split()[0]

            if child == None:
                child = f'Group/Chat/{d}'

            with open('data.json', 'w', encoding ='utf8') as json_file:
                json.dump(self.pull(child), json_file, ensure_ascii = False)

        else:
            error = '\n...Wrong Credentials !!!\n'
            print(error)
            return error

# link = 'https://chatting-c937e-default-rtdb.firebaseio.com/'
# obj = vicks(link)

# f = obj.show()
# f = obj.pull()
# f = obj.push(1)
# f = obj.remove()

# print(f)
# input('Press Enter to Exit...')

# def recommendation (vid):
#     from multivicks import crud as c
#     import pandas as pd
#
#     obj = c.vicks('@Hey_Vicks',
#         link = 'https://quickstart-1578034411252.firebaseio.com/')
#
#     obj.add(vid, 'Video/Views')
#     vlist = list(obj.pull('Video/Views').values())
#
#     counts = pd.Series(vlist).value_counts()
#     vdict = dict(counts.items())
#
#     recommend = list(vdict.keys())
#     return recommend

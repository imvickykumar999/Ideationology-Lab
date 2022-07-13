
# https://pastebin.com/asRbutde

import requests # see https://2.python-requests.org/en/master/
 
key = 'CA9w42R6EP2mpEnPbdGiPWgRcE9DrIhu'

source_code = '''
print("Hello, world!")
a = 1
b = 2
print(a + b)
'''

t_title = "using api"
 
login_data = {
    'api_dev_key': key,
    'api_user_name': 'vickykumar999',
    'api_user_password': 'ytExSH*QnYg8q9m'
    }

data = {
    'api_option': 'paste',
    'api_dev_key':key,
    'api_paste_code':source_code,
    'api_paste_name':t_title,
    'api_paste_expire_date': 'N',
    'api_user_key': None,
    'api_paste_format': 'python'
    }
 
# We have 9 valid values available which you can use with the 'api_paste_expire_date' parameter:
#     N = Never
#     10M = 10 Minutes
#     1H = 1 Hour
#     1D = 1 Day
#     1W = 1 Week
#     2W = 2 Weeks
#     1M = 1 Month
#     6M = 6 Months
#     1Y = 1 Year

login = requests.post("https://pastebin.com/api/api_login.php", data=login_data)
print("Login status: ", login.status_code if login.status_code != 200 else "OK/200")
print("User token: ", login.text)
data['api_user_key'] = login.text
 
r = requests.post("https://pastebin.com/api/api_post.php", data=data)
print("Paste send: ", r.status_code if r.status_code != 200 else "OK/200")
print("Paste URL: ", r.text)
 
 
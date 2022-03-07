
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

web = webdriver.Chrome()
web.get('https://ideationology.herokuapp.com/login/')

def fun_login(passw):
    try:
        Email = passw = "imvickykumar"
        time.sleep(2) # on login page...

        first = web.find_element(By.XPATH, '//*[@id="username"]')
        first.send_keys(Email)

        last = web.find_element(By.XPATH, '//*[@id="password"]')
        last.send_keys(passw)

        Submit = web.find_element(By.XPATH, '//*[@id="login"]/input[3]')
        Submit.click()

        time.sleep(2) # on profile page...
        amount = 1
        account = 'imvickykumar999'

        first = web.find_element(By.XPATH, '/html/body/center[2]/div/div/div[1]/div[5]/form/div/input[1]')
        first.send_keys(amount)

        last = web.find_element(By.XPATH, '/html/body/center[2]/div/div/div[1]/div[5]/form/div/input[2]')
        last.send_keys(account)        
        
        Submit = web.find_element(By.XPATH, '/html/body/center[2]/div/div/div[1]/div[5]/form/input')
        Submit.click()

        # print(passw)
    except:
        web.refresh()

fun_login(passw)


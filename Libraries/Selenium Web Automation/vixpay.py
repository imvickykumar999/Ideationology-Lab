
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

web = webdriver.Chrome()
web.get('http://127.0.0.1:5000/login/')

Email = "imvickykumar"
amount = 1
account = 'imvickykumar999'

def fun_login(passw):
    try:
        time.sleep(2) # on login page...
        first = web.find_element(By.XPATH, '//*[@id="username"]')
        first.send_keys(Email)

        last = web.find_element(By.XPATH, '//*[@id="password"]')
        last.send_keys(passw)

        Submit = web.find_element(By.XPATH, '//*[@id="login"]/input[3]')
        Submit.click()

        for _ in range(2):
            time.sleep(2) # on profile page...
            first = web.find_element(By.XPATH, '/html/body/center[2]/div/div/div[1]/div[5]/form/div/input[1]')
            first.send_keys(amount)

            last = web.find_element(By.XPATH, '/html/body/center[2]/div/div/div[1]/div[5]/form/div/input[2]')
            last.send_keys(account)        
            
            Submit = web.find_element(By.XPATH, '/html/body/center[2]/div/div/div[1]/div[5]/form/input')
            Submit.click()

        Logout = web.find_element(By.XPATH, '/html/body/center[2]/div/div/div[1]/div[6]/a/h3')
        Logout.click()
        
    except:
        # web.refresh()
        pass

for _ in range(2):
    passw = "imvickykumar"
    fun_login(passw)


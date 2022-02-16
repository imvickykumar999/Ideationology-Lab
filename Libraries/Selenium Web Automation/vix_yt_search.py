
from selenium import webdriver
import time, sys

web = webdriver.Chrome()
web.get('https://vixtest.herokuapp.com/youtube')
time.sleep(3)

try:
    mess = sys.argv[1]
except:
    mess = "despacito"

fill_it = web.find_element_by_xpath('/html/body/center/div[1]/form/div/div/input')
fill_it.send_keys(mess)

Submit = web.find_element_by_xpath('/html/body/center/div[1]/form/div/input')
Submit.click()

# ----------------------------------------

import pyautogui

# pos = pyautogui.position()
# print(pos)

time.sleep(2)
pyautogui.click(659, 972) # play
pyautogui.click(1228, 31) # maximize

# time.sleep(1)
# pyautogui.click(1769, 19) # minimize



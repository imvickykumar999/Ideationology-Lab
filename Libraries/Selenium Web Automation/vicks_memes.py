
from selenium import webdriver
import time

web = webdriver.Chrome()
web.get('https://imvickykumar999.herokuapp.com/vixmemes#vickscroll')
time.sleep(3)

mid = "87743020"
memeid = web.find_element_by_xpath('/html/body/div[4]/div/center/div/form/center/div/div[1]/input')
memeid.send_keys(mid)

mid = "C++"
memeid = web.find_element_by_xpath('/html/body/div[4]/div/center/div/form/center/div/div[2]/input')
memeid.send_keys(mid)

mid = "Python"
memeid = web.find_element_by_xpath('/html/body/div[4]/div/center/div/form/center/div/div[3]/input')
memeid.send_keys(mid)

Submit = web.find_element_by_xpath('/html/body/div[4]/div/center/div/form/center/div/input')
Submit.click()

share_it = web.find_element_by_xpath('/html/body/div[3]/div[2]/center/a/h1/strong')
share_it.click()
time.sleep(5)

import pyautogui
pos = pyautogui.position()
print(pos)

pyautogui.click(824, 296) # mini close


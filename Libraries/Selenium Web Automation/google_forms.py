# https://www.youtube.com/watch?v=YbGAUEjTKg4
# https://pypi.org/project/pywhatkit/

from selenium import webdriver
import time

web = webdriver.Chrome()
web.get('https://docs.google.com/forms/d/e/1FAIpQLSdHkENv2WcTzvoXtqQ3UbIdxmcEPRxhD6LqGqlz4it4Ts3qgg/viewform')
time.sleep(3)

# RadioButtonPeriod = web.find_element_by_xpath('//*[@id="i11"]/div[3]/div') # correct answer
RadioButtonPeriod = web.find_element_by_xpath('//*[@id="i8"]/div[3]/div') # incorrect answer
RadioButtonPeriod.click()

# Email = "imvickykumar999@gmail.com"
# first = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input')
# first.send_keys(Email)

Answer = "Tuple has no Attribute called append and pop."
last = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
last.send_keys(Answer)

Submit = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
Submit.click()

get_confirmation_div_text = web.find_element_by_css_selector('.freebirdFormviewerViewResponseConfirmationMessage')
# print(get_confirmation_div_text.text)

viewscore = web.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/div/a/span/span')
viewscore.click()

if ((get_confirmation_div_text.text) == "Your response has been recorded"):
    print ("Test Was Successful")
else:
    print("Test Was Not Successful")


# https://stackoverflow.com/a/27046948/11493297

import pyautogui
# pos = pyautogui.position()
# print(pos)

# pyautogui.click(1286, 31) # mini close
pyautogui.click(1228, 28) # maximize
# pyautogui.click(1882, 19) # close maxi

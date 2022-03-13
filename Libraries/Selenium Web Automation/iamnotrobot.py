# https://www.youtube.com/watch?v=YbGAUEjTKg4
# https://pypi.org/project/pywhatkit/

from selenium import webdriver
import time

web = webdriver.Chrome()
web.get('https://pythonprogramminglanguage.com/text-to-speech/')
time.sleep(3)

Email = "imvickykumar999@gmail.com"
first = web.find_element_by_xpath('//*[@id="contact-form-email"]')
first.send_keys(Email)

Answer = '''
This Comment is written by Selenium web Automation Code.
File name is "i_am_not_a_robot.py"
'''
last = web.find_element_by_xpath('//*[@id="contact-form-message"]')
last.send_keys(Answer)

recaptcha = web.find_element_by_xpath('//*[@id="recaptcha-anchor"]/div[1]')
recaptcha.click()

Submit = web.find_element_by_xpath('//*[@id="simple-contact-form"]/p[4]/button')
Submit.click()


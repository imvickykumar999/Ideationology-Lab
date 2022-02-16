
from selenium import webdriver
import time

web = webdriver.Chrome()
web.get('https://vixtest.herokuapp.com/bot')
time.sleep(3)

mess = "This message is sent with Web Automation using Selenium."
fill_it = web.find_element_by_xpath('/html/body/center/div/form/div/div[1]/input')
fill_it.send_keys(mess)

mess = "https://chat.googleapis.com/v1/spaces/AAAAJd5Znh4/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=-kNINNTwvbG1nKS04yfeSWT9ZCF7eNc0hO_4MwOr5gE%3D"
fill_it = web.find_element_by_xpath('/html/body/center/div/form/div/div[2]/input')
fill_it.send_keys(mess)

Submit = web.find_element_by_xpath('/html/body/center/div/form/div/a')
Submit.click()

time.sleep(2)

mess = "https://images.squarespace-cdn.com/content/v1/56a9d6e3a2bab82578144fc2/1605709952940-4CEAI0WSSDOQIXQ588IO/StoryTellersAndStorySellersEp46.png?format=1000w"
fill_it = web.find_element_by_xpath('//*[@id="detail"]/div/div/div[1]/input')
fill_it.send_keys(mess)

mess = "https://www.instagram.com/p/CaCgA6NPQfo/"
fill_it = web.find_element_by_xpath('//*[@id="detail"]/div/div/div[2]/input')
fill_it.send_keys(mess)

Submit = web.find_element_by_xpath('/html/body/center/div/form/div/input')
Submit.click()

# expand_it = web.find_element_by_xpath('//*[@id="navbarDropdown"]')
# expand_it.click()


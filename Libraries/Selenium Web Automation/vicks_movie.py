
from selenium import webdriver
import time

web = webdriver.Chrome()
web.get('https://imvickykumar999.herokuapp.com/movies#vickscroll')
time.sleep(3)

Coupon_Code = "PUSHPA.VICKS"
fill_it = web.find_element_by_xpath('/html/body/div[3]/div/center/form/div/div/input')
fill_it.send_keys(Coupon_Code)

Submit = web.find_element_by_xpath('/html/body/div[3]/div/center/form/div/input')
Submit.click()

expand_it = web.find_element_by_xpath('//*[@id="navbarDropdown"]')
expand_it.click()


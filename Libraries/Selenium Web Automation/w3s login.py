from selenium import webdriver
import time

web = webdriver.Chrome()
Email = "sagar.sws2000@gmail.com"
# Email = "18erecs080.vicky@rietjaipur.ac.in"
passw = "Hellovix999@"

def fun_signup():
    web.get('https://www.w3schools.com/')
    time.sleep(4)

    login = web.find_element_by_xpath('//*[@id="w3loginbtn"]')
    login.click()

    signup = web.find_element_by_xpath('//*[@id="root"]/div/div/div[4]/div[1]/div/div[2]/form/div[1]/div[1]/span/span')
    signup.click()

    first = web.find_element_by_xpath('//*[@id="modalusername"]')
    first.send_keys(Email)

    last = web.find_element_by_xpath('//*[@id="new-password"]')
    last.send_keys(passw)

    Submit = web.find_element_by_xpath('//*[@id="root"]/div/div/div[4]/div[1]/div/div[4]/div[1]/button')
    Submit.click()

    fname = "Vicky"
    first = web.find_element_by_xpath('//*[@id="modal_first_name"]')
    first.send_keys(fname)

    lname = "Kumar"
    last = web.find_element_by_xpath('//*[@id="modal_last_name"]')
    last.send_keys(lname)

    Submit = web.find_element_by_xpath('//*[@id="root"]/div/div/div[4]/div[1]/div/div[3]/div/button')
    Submit.click()

# fun_signup()


def fun_login():
    web.get('https://my-learning.w3schools.com/')
    time.sleep(4)

    first = web.find_element_by_xpath('//*[@id="modalusername"]')
    first.send_keys(Email)

    last = web.find_element_by_xpath('//*[@id="current-password"]')
    last.send_keys(passw)

    Submit = web.find_element_by_xpath('//*[@id="root"]/div/div/div[4]/div[1]/div/div[4]/div[1]/button')
    Submit.click()

    # time.sleep(10)
    # logout = web.find_element_by_xpath('//*[@id="navigation"]/div/button')
    # logout.click()
    # fun_login()

fun_login()

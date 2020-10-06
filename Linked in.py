import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.firefox.webdriver import WebDriver

print('Enter Role!!!')
Role = input()


print('How many invites you want to send!!')
Invites_count = input()

print('-------------------------------------------------')

print('Enter note you want to send to invites!!!')
Invite_note = input()

print('-------------------------------------------------')

print('Browser Launch!!!!')
browser=webdriver.Chrome(executable_path=("D:\SeleniumProject\Web_drivers\chromedriver"))
#browser= webdriver.Firefox()
browser.maximize_window()
browser.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin/')
browser.find_element_by_name("session_key").send_keys("")
browser.find_element_by_name("session_password").send_keys("")
browser.find_element_by_xpath("//button[text()='Sign in']").click()

time.sleep(2)
i = 0
for j in range(0 , int(Invites_count)):
    browser.get('https://www.linkedin.com/search/results/people/?keywords={0}&page={1}'.format(Role, str(j))
    )
    Connection = browser.find_elements_by_xpath("//button[text()='Connect']")
    time.sleep(2)
    #count = count + 1
    for conn in Connection:
        conn.click()
        browser.find_element_by_xpath("//span[text()='Add a note']").click()
        time.sleep(2)
        browser.find_element_by_id("custom-message").send_keys(Invite_note)
        browser.find_element_by_xpath("//span[text()='Done']").click()
        time.sleep(5)
        i=i+1
        if i == int(Invites_count):
            break
    if i == int(Invites_count):
        break
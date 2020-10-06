from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path=("D:\SeleniumProject\Web_drivers\chromedriver.exe"))
driver.maximize_window()
driver.get("https://www.facebook.com/")
# wait for sometime (Wait for all the elements on the page to be visible)

driver.implicitly_wait(10)

assert  "Facebook – log in or sign up" in driver.title

driver.find_element_by_name("email").send_keys("")
driver.find_element_by_name("pass").send_keys("")
driver.find_element_by_name("login").click()
time.sleep(5)
driver.quit()
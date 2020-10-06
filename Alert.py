from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="D:\SeleniumProject\Web_drivers\chromedriver")
driver.maximize_window()
driver.get("http://testautomationpractice.blogspot.com/")
driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[2]/div/aside/div/div[2]/div[1]/button").click()
time.sleep(2)
#driver.switch_to_alert().accept() # Closes alert window with "OK" button
driver.switch_to_alert().dismiss() # Closes alert window with "Cancel" button
time.sleep(5)
driver.quit()
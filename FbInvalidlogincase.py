from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s= Service("C:\Drivers\chromedriver_win32\chromedriver")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://www.facebook.com/")
time.sleep(2)
driver.find_element(By.ID, "email").send_keys("Test User")
time.sleep(1)
driver.find_element(By.ID,"pass").send_keys("12345678")
time.sleep(1)
driver.find_element(By.NAME,"login").click()
time.sleep(8)
driver.close()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path=("D:\SeleniumProject\Web_drivers\chromedriver.exe"))
driver.maximize_window()
driver.get("https://www.youtube.com/")
print(driver.title)
print(driver.current_url)
driver.forward()

driver.get("https://www.google.com/")
driver.back()
driver.forward()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='gbw']/div/div/div[1]/div[1]/a").click()
time.sleep(5)

driver.quit()
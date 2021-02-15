from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import ActionChains

driver=webdriver.Firefox(executable_path="D:\SeleniumProject\Web_drivers\geckodriver.exe")
driver.maximize_window()
driver.get("http://testautomationpractice.blogspot.com/")
driver.find_element_by_xpath("//*[@id='field1']").clear()
driver.find_element_by_xpath("//*[@id='field1']").send_keys("Testing")
Copybutton=driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")
action=ActionChains(driver)
action.double_click(Copybutton).perform()
driver.implicitly_wait(10)
time.sleep(3)
driver.close()




from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import ActionChains

driver=webdriver.Firefox(executable_path="D:\SeleniumProject\Web_drivers\geckodriver.exe")
driver.maximize_window()
driver.get("http://testautomationpractice.blogspot.com/")
driver.execute_script("window.scrollBy(0,700)","")
source_element=driver.find_element_by_xpath("//*[@id='gallery']/li[1]/img")
target_element=driver.find_element_by_xpath("//*[@id='trash']")
action=ActionChains(driver)
action.drag_and_drop(source_element, target_element).perform()
time.sleep(2)
driver.execute_script("window.scrollBy(700,-350)","")
source2=driver.find_element_by_xpath("//*[@id='draggable']")
target2=driver.find_element_by_xpath("//*[@id='droppable']")
action.drag_and_drop(source2, target2).perform()
time.sleep(3)
driver.close()




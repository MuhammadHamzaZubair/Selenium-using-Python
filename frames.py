from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="D:\SeleniumProject\Web_drivers\chromedriver")
driver.maximize_window()
driver.get("https://www.selenium.dev/selenium/docs/api/java/")
time.sleep(2)
driver.switch_to.frame("packageListFrame") # First frame
driver.find_element_by_link_text("com.thoughtworks.selenium").click()
driver.switch_to.default_content()
driver.switch_to.frame("packageFrame") #Second frame
time.sleep(2)
driver.find_element_by_link_text("BrowserConfigurationOptions").click()
driver.switch_to.default_content()
driver.switch_to.frame("classFrame")
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/ul/li[5]/a").click()
time.sleep(3)
driver.close()
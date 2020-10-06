from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#driver = webdriver.Firefox(executable_path="D:\SeleniumProject\Web_drivers\geckodriver.exe")
driver = webdriver.Chrome(executable_path="D:\SeleniumProject\Web_drivers\chromedriver")
#driver = webdriver.Ie(executable_path="D:\SeleniumProject\Web_drivers\IEDriverServer")
driver.maximize_window()
driver.get("https://abaadee.com/my-account/")
print(driver.title)
print(driver.current_url)
driver.find_element_by_xpath("/html/body/div[1]/header/div[2]/div[1]/div[3]/div[3]/a").click()
time.sleep(5)
driver.close()

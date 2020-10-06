from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(executable_path="D:\SeleniumProject\Web_drivers\chromedriver")
driver.maximize_window()
#driver.get("https://www.facebook.com/")
driver.get("https://www.keynotesupport.com/internet/web-contact-form-example-radio-buttons.shtml")
#email_ele=driver.find_element_by_name("email")
#print("Email Element")
#print("--------------")
#print(email_ele.is_displayed())
#print(email_ele.is_enabled())
#print("")
#print("Password Element")
#print("-----------------")
#pass_ele2=driver.find_element_by_name("pass")
#print(pass_ele2.is_displayed())
#print(pass_ele2.is_enabled())

#email_ele.send_keys("")
#time.sleep(3)
#pass_ele2.send_keys("")
#time.sleep(3)
#driver.find_element_by_name("login").click()

radio=driver.find_element_by_css_selector("input[value=Excel]")
print(radio.is_enabled()) #Main conditional commands
print(radio.is_displayed())
print(radio.is_selected())
time.sleep(5)
driver.close()
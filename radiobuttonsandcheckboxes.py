from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver=webdriver.Chrome(executable_path="D:\SeleniumProject\Web_drivers\chromedriver")
driver.maximize_window()
#driver.get("https://www.facebook.com/")
driver.get("https://www.ericmmartin.com/code/jquery/checkbox.html")
#driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[5]").click()
driver.implicitly_wait(10)
#time.sleep(4)

#Working with check boxes
#status3=driver.find_element_by_id("test-3").click()
checkbox=driver.find_element_by_id("test-3").is_selected()
print("\nCheck box is selected or not?")
print("--------------------------------")
print(checkbox)
time.sleep(3)


# Working with raio buttons
#status=driver.find_element(By.CSS_SELECTOR,"input[type=radio]").click()
#status1=driver.find_element_by_id("").click()
#time.sleep(5)
#status1=driver.find_element_by_class_name("_8esa").is_selected()
#print("\nIs selected or not?" )
#print("----------------------" )
#print(status1)
driver.quit()
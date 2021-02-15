from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Firefox(executable_path="D:\SeleniumProject\Web_drivers\geckodriver.exe")
driver.maximize_window()
driver.get("https://www.healthsolutions.com.pk/")
time.sleep(3)
#Scrolling till a particular position
#driver.execute_script("window.scrollBy(0,1000)","")

#Ambulance=driver.find_element_by_xpath("/html/body/div[8]/div/div[2]/div/a[1]/div/div/div/p[3]")
Ambulance=driver.find_element_by_css_selector(".w3-border-izza")

#Scrolling till the identification of a particular element
driver.execute_script("arguments[0].scrollIntoView();",Ambulance)
#Scrolling till the end of page
#driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(5)
driver.close()



















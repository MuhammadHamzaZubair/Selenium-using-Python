from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="D:\SeleniumProject\Web_drivers\chromedriver")
driver.maximize_window()
driver.get("https://www.healthsolutions.com.pk/")
links=driver.find_elements(By.TAG_NAME,"a")
print("Number of links present:",len(links)) # Prints the no of links in the page
for link in links:
    print(link.text)

#Clicking on the link
#driver.find_element(By.LINK_TEXT,"SERVICES").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Genral").click()
time.sleep(5)
driver.quit()
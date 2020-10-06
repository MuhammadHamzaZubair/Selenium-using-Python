from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(executable_path="D:\SeleniumProject\Web_drivers\chromedriver")
driver.maximize_window()
driver.get("https://www.facebook.com/")
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[5]").click()
driver.implicitly_wait(5)
element=driver.find_element_by_id("day")
drp=Select(element)
# Selection of value by visible text
drp.select_by_visible_text("29")
element2=driver.find_element_by_id("month")
drp2=Select(element2)
drp2.select_by_visible_text("Apr")

# Select by index
drp.select_by_index("9")

# Select by value
drp2.select_by_value("4")
time.sleep(5)

# Capture all the options from the drop down and print
all_options=drp2.options
for option in all_options:
    print(option.text)
# Count number of options with in a drop down
#print(len(drp2.options))
driver.quit()
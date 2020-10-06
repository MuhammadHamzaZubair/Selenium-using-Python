from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(executable_path="D:\SeleniumProject\Web_drivers\chromedriver")
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.current_window_handle)
time.sleep(3)
driver.find_element_by_link_text("click").click()
handles=driver.window_handles # will return all the handle values of the opened browser windows
for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title=="Frames & windows":
        driver.close()
        time.sleep(5)
driver.quit()

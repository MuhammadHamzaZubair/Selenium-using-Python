from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="D:\SeleniumProject\Web_drivers\geckodriver.exe")
driver = webdriver.Chrome(executable_path="D:\SeleniumProject\Web_drivers\chromedriver")
driver = webdriver.Ie(executable_path="D:\SeleniumProject\Web_drivers\IEDriverServer")
driver.maximize_window()
driver.get("https://abaadee.com/my-account/")
print(driver.title)
print(driver.current_url)
print(driver.page_source)
#driver.close()
driver.quit()




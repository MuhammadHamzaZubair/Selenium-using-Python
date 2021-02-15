from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

driver = webdriver.Firefox(executable_path="D:\SeleniumProject\Web_drivers\geckodriver.exe")
driver.maximize_window()
driver.get("https://www.healthsolutions.com.pk/")

time.sleep(3)
driver.find_element_by_css_selector("#page-top > div.navigation-4.fsnm.fixedNavbar > div > div > div.col-md-10.col-sm-10.col-xs-12 > nav > div.collapse.navbar-collapse.nav-collapse > ul > a.login").click()
driver.implicitly_wait(10)
driver.find_element_by_xpath("//*['@id=logForm']/fieldset/div[1]/input").send_keys("hamza@engitechservices.com")
driver.find_element_by_xpath("//*[@id='logForm']/fieldset/div[2]/input").send_keys("123456")
driver.find_element_by_xpath("//*[@id='logForm']/fieldset/button").click()
time.sleep(10)
Services=driver.find_element_by_css_selector("#navbarDropdown")
Ambulance=driver.find_element_by_css_selector("#page-top > div.navigation-4.fsnm.fixedNavbar > div > div > div.col-md-10.col-sm-10.col-xs-12 > nav > div.collapse.navbar-collapse.nav-collapse > ul > li.nav-item.dropdown.hover > div > a:nth-child(1)")
Blood=driver.find_element_by_css_selector("#page-top > div.navigation-4.fsnm.fixedNavbar > div > div > div.col-md-10.col-sm-10.col-xs-12 > nav > div.collapse.navbar-collapse.nav-collapse > ul > li.nav-item.dropdown.hover > div > a:nth-child(3)")
actions=ActionChains(driver)
actions.move_to_element(Services).move_to_element(Ambulance).move_to_element(Blood).move_to_element(Ambulance).click().perform()
time.sleep(10)
driver.close()

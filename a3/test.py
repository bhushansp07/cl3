from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://localhost:5000")
elem = driver.find_element_by_name("text1")
elem1 = driver.find_element_by_name("text2")
elem.send_keys("4")
elem1.send_keys("3")
elem.send_keys(Keys.RETURN)
assert "12" in driver.page_source
driver.close()


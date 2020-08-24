from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.google.com")
abc=driver.find_element_by_class_name("gsfi")
ActionChains(driver).move_to_element(abc).context_click(abc).perform()
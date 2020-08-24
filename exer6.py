from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains 

driver=webdriver.Firefox()
driver.get("http://www.airindia.in/")
abc=driver.find_element_by_xpath("//*[@id='aMnu3']")
ActionChains(driver).move_to_element(abc).perform()
driver.implicitly_wait(5)
xyz=driver.find_element_by_xpath("/html/body/form/div[3]/div/div[1]/div[1]/div[3]/div/div[1]/ul/li[4]/div/ul/li[6]/a")
ActionChains(driver).move_to_element(xyz).click(xyz).perform()
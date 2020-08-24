from selenium import webdriver
driver=webdriver.Firefox()
driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_alert")
driver.find_element_by_xpath("/html/body/button").click()
driver.switch_to_alert().accept()



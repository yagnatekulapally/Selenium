from selenium import webdriver

driver=webdriver.Firefox()
driver.get("https://www.google.com")
print(driver.current_url)
print(driver.title)

driver.get("https://www.facebook.com")
print(driver.current_url)
print(driver.title)

driver.back()
print(driver.current_url)
driver.forward()
print(driver.current_url)
driver.refresh()
driver.maximize_window()

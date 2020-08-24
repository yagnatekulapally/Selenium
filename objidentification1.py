from selenium import webdriver

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.gmail.com")
print(driver.current_url)
print(driver.title)
#enter gmail id
driver.find_element_by_id("identifierId").send_keys("yagna.tekulapally@gmail.com")
#click on the button
driver.find_element_by_id("identifierNext").click()
#enter the password
driver.implicitly_wait(5)
driver.find_element_by_name("password").send_keys("Yagna123")
#sign in
driver.implicitly_wait(5)

#driver.find_element_by_xpath("//*[@id='passwordNext']").click()

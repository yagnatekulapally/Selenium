from selenium import webdriver
chromedriverpath="C:\Yagna\chrome driver\chromedriver_win32\chromedriver.exe"
driver=webdriver.Chrome(chromedriverpath)
driver.get("https:\\www.facebook.com")
print (driver.current_url)
driver.find_element_by_name("firstname").send_keys("yagna")
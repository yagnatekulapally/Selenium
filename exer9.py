from selenium import webdriver

chromedriverpath="C:\Yagna\chrome driver\chromedriver_win32\chromedriver.exe"
driver=webdriver.Chrome(chromedriverpath)
driver.get("http://www.google.com")
driver.save_screenshot("F:\home.png")
driver.get("http://www.facebook.com")
driver.save_screenshot("F:\fb.png")

from selenium import webdriver


chromedriverpath="C:\Yagna\chrome driver\chromedriver_win32\chromedriver.exe"
driver=webdriver.Chrome(chromedriverpath)
driver.get("http://jqueryui.com/tooltip/")
fra=driver.find_element_by_xpath("//*[@id='content']/iframe")
driver.switch_to_frame(fra)
driver.find_element_by_id("age").send_keys("16")
driver.switch_to_default_content()
driver.find_element_by_link_text("Draggable").click()
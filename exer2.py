from selenium import webdriver
from selenium.webdriver.support.ui import Select
from select import select
chromedriverpath="C:\Yagna\chrome driver\chromedriver_win32\chromedriver.exe"
driver=webdriver.Chrome(chromedriverpath)

driver.get("http://www.airindia.in/")
driver.find_element_by_xpath("/html/body/form/div[3]/div/div[1]/div[2]/div[3]/ul/li[1]/a")     
driver.find_element_by_xpath("/html/body/form/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/ul[3]/li[1]/fieldset/div[1]/label").click()
driver.find_element_by_id("from").send_keys("ban")
driver.implicitly_wait(4)
#driver.find_element_by_xpath("//*[@id='ui-id-130']").click()
driver.find_element_by_partial_link_text("Bangkok").click()
driver.implicitly_wait(4)
driver.find_element_by_xpath("//*[@id='to']").send_keys("del")
driver.implicitly_wait(4)
driver.find_element_by_partial_link_text("Delhi").click()

dropdown=Select(driver.find_element_by_xpath("//*[@id='_classType1']"))

dropdown.select_by_index(3)
print(driver.find_element_by_xpath("/html/body/form/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/ul[5]/li[3]/div[5]/span/span").text)
radio=driver.find_element_by_id("rdrules1")
if radio.is_selected():
    print("True")
else:
    print("false")
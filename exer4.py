from selenium import webdriver
driver=webdriver.Firefox()
driver.get("https://www.ebay.com/")

abc=driver.find_elements_by_tag_name("a")
print(len(abc))
xyz=driver.find_element_by_id("glbfooter")

zyx=xyz.find_elements_by_tag_name("a")
print(len(zyx))

for a in zyx:
    print(a.text)

"""from selenium import webdriver

#chromedriverpath= "C:\chromedriver.exe"

driver=webdriver.Firefox()

driver.get("https://paytm.com/")

driver.find_element_by_xpath("//input[contains(@id,'mobile')]").send_keys("96766")

driver.find_element_by_css_selector("[id*='amou']").send_keys("400")"""

 


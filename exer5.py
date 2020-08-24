"""from selenium import webdriver
driver=webdriver.Firefox()
driver.get("https://accounts.google.com/SignUp?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F")
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/p/a").click()

print( driver.title)
parent=driver.current_window_handle
driver.switch_to_window(driver.window_handles[-1])
child=driver.current_window_handle
print(driver.title)
driver.switch_to_window(parent)"""
from selenium import webdriver



driver=webdriver.Firefox();

driver.get("https://accounts.google.com/signup")

driver.find_element_by_xpath("html/body/div[1]/div[2]/div/div[1]/p/a").click()

print("Before Switching")

print(driver.title)

parent_window = driver.window_handles[0]

child_window = driver.window_handles[1]

driver.switch_to_window(child_window)

print("After Switching")

print(driver.title)

driver.switch_to_window(parent_window)

print("Switch Back to Parent")

print(driver.title)
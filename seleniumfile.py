f=open('F:\\url.txt','r')
lines=f.readlines()
from selenium import webdriver
driver=webdriver.Firefox()
print(lines)
driver.get(lines[1])
f.close()
#from selenium import webdriver
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
df = pd.read_excel('F:\\test.xlsx', sheet_name='Sheet1')
 
print("Column headings:")
print(df.columns)
lines=df.columns


#driver=webdriver.Firefox()
#driver.get(lines[1])

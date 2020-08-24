import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_excel('F:\\test.xlsx', sheet_name='Sheet1')
print(df.columns)



df1=df.head(2)
df2=df.tail(2)
print(df.head(2))
print("------------------------------------")
print(df.tail(2))
print("------------------------------------")

merge=pd.merge(df1,df2)
print(merge)
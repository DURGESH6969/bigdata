import pandas as pd
df1=pd.read_csv("16.csv")
print(df1)
newRow={}
name=input("Enter name: ")
stream=input("Enter stream: ")
year=input("Enter year: ")
newRow['NAME']=name
newRow['STREAM']=stream
newRow['YEAR']=year
print(newRow)
df1=df1.append(newRow,ignore_index=True)
df1.to_csv("16.csv",index=False)
import pandas as pd
list=[]
n=int(input("Enter the size of the list: "))
print("Enter the values: ")
for i in range(n):
    list.append(int(input()))
series=pd.Series(list)
print("Original Series: ")
print(series)
print("Enter the custom labels: ")
labels=[]
for i in range(n):
    labels.append(input())
series.index=labels 
print("Series with custom labels: ")
print(series)
print("Keys:",series.keys())
print("Values: ",series.values)
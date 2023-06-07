import pandas as pd
n=int(input("enter the number of elemnents: "))
list1=[]
list2=[]
print("Enter elements of first list: ")
for i in range(n):
    list1.append(int(input()))
print("Enter elements of second list: ")
for i in range(n):
    list2.append(int(input()))   
Series1=pd.Series(list1)
Series2=pd.Series(list2)
print("Addition: ")
print(Series1+Series2)
print("Subtraction: ")
print(Series1-Series2)
print("Multiplication: ")
print(Series1*Series2)
print("Division: ")
print(Series1/Series2)
import pandas
mydict={ }
l=[ ]
n=int(input("Enter the number of inputs: "))
for i in range(1,n+1):
    l=[ ]
    print("Enter the row: ",i)
    for j in range(n):
        l.append(input("Enter the values: "))
    mydict[i]=l
print(mydict)
ds=pandas.Series(mydict)
print(ds)    
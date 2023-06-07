import pandas
dictionary={}
n=int(input("Enter number of keys: "))
for i in range(n):
    temp=[]
    m=int(input("Enter the number of elements in value list%s: " %(i+1)))
    print("Enter values: ")
    for j in range(m):
        temp.append(int(input()))
    dictionary[i]=temp;
df=pandas.DataFrame(dictionary)
print("\nDataFrame: ")
print(df)
series=df.iloc[-2:,1:2]
print("Second col of last rows: ")
print(series)        
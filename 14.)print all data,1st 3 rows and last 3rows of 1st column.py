import pandas
df=pandas.read_csv("14.csv")
print("The student data is: ")
print(df)
print("First 3 rows are: ")
print(df.head(3))
print("Last 3 rows of first column are: ")
print(df.tail(3))

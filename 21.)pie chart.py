import matplotlib.pylab as plt
import pandas as pd
df1=pd.read_csv("21.csv")
print(df1)
list1=list(df1.columns)
print(list1)
piechart= df1.groupby(list1[1])[list1[3]].mean()
piechart.plot(kind='pie',y=list1[2],autopct='%1.0f%%')
plt.title("Assignment-21")
plt.show()
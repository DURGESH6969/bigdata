import matplotlib.pylab as plt
import pandas as pd
df1=pd.read_csv("20.csv")
print(df1)
list1=[]
for i in df1.columns:
    list1.append(i)
print(list1)
ax=df1.plot.bar(x=list1[0],y=list1[2],rot=0,color='blue')
plt.title("Assignment-20")
plt.show()    
    

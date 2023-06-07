import matplotlib.pyplot as pt
x=[]
y=[]
n=int(input("Enter the number of points: "))
for i in range(n):
    x.append(int(input("Enter x: ")))
    y.append(int(input("Enter y: ")))
pt.plot(x,y,'--g')
pt.xlabel("X-axis")    
pt.ylabel("Y-axis")
pt.title("Assignment 17")
pt.show()
import matplotlib.pylab as plt
import numpy as np
x=np.linspace(-5,10,5)
m=int(input("Enter the slope: "))
c=int(input("Enter the constant: "))
y=m*x+c
plt.plot(x,y,'*--r')
plt.title("Assignment 18")
plt.show()

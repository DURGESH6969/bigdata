import numpy as np
arr=[]
n=int(input("Enter the size of the matrix: "))
for i in range(n):
    for j in range(n):
        arr.append(int(input("Enter value: ")))        
a=np.array(arr).reshape(n,n)
print("Original matrix: ")
print(a)
print("Sorted along first matrix: ")
print(np.sort(a,axis=0))
print("Sorted along last axis: ")
print(np.sort(a,axis=1))
print("Sorted and Flattend: ")
print(np.sort(a,axis=None))
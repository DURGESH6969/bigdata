import numpy as np
m=int(input("Enter the no. of rows: "))
n=int(input("Enter the no. of columns: "))
matrix=[]
for i in range(0,n):
    temp=[]
    for j in range(0,m):
        temp.append(int(input("Enter elements: ")))
    matrix.append(temp)
print("The original matrix is: ",np.array(matrix))
print("Minimum element in the matrix is: ",np.min(matrix))
print("Maximum element in the matrix is: ",np.max(matrix)) 
rowsort=np.sort(matrix,axis=1)
print("Row wise sorted: ",rowsort)
colsort=np.sort(matrix,axis=0)
print("Column wise sorted: ",colsort)   
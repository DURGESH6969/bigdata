import numpy as np
iden=np.identity(4)
print(iden)
mat1=[]
mat2=[]
for i in range(2):
    for j in range(2):
        mat1.append(int(input("Enter the values: ")))
matrix1=np.array(mat1).reshape(2,2)
print("Matrix1: ")
print(matrix1)
for i in range(2):
    for j in range(2):
        mat2.append(int(input("Enter the values: ")))   
matrix2=np.array(mat2).reshape(2,2)
print("Matrix2: ")
print(matrix2)
result=np.add(matrix1,matrix2)
print("Addition result: ")
print(result)
t=matrix1.transpose()
print("Transpose of Matrix1: ")
print(t)
n=np.dot(t,matrix2)
print("Multiplication result(Transpose*Matrix2): ")
print(n)        
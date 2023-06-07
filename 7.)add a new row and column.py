import numpy as np
matrix=[]
for i in range(3):
    for j in range(3):
        matrix.append(int(input("Enter values: ")))
arr=np.array(matrix).reshape(3,3)
print("Original matrix: ")
print(arr)
new_row=np.array([1,2,3])
arr=np.row_stack((arr,new_row))
print("Array after adding row: ")
print(arr)
new_column=np.array([1,2,3,4])
arr=np.column_stack((arr,new_column))    
print("Array after adding column: ")
print(arr)   
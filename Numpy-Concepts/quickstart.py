import numpy as np


#Array in numpy(One dimension)
a = np.array([1,2,3,4,5,6,7,8,9])

#Acessing one element in array 
a[0]



#Matrix 2x2 (Two dimensions)
m = np.array([[1,2],[3,4]])

#Acessing one element in matrix 
m[0,1]


matrix_3d = np.array([
    [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12]],

    [[13, 14, 15, 16],
     [17, 18, 19, 20],
     [21, 22, 23, 24]]
])



print("Array = ")
print(a)

print("Matrix = ")
print(m)


print("3d Matrix = ")
print(matrix_3d)
print(f"Shape: {matrix_3d.shape}")
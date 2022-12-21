import numpy as np
import os

os.system('cls')

# Given 3 vectors
vector_u = np.array([1.0,2.0,3.0])
vector_v = np.array([4.0,1.0,-2.0])
vector_w = np.array([-3.0,7.0,4.5])

# Matrix from 3 vectors
matrix = np.column_stack((vector_u, vector_v, vector_w))

# Print Matrix
print("Matrix:")
print(matrix)

# Shape of Matrix
print("Shape of matrix:")
print(matrix.shape)

# Print third column
print("Third column:")
print(matrix[:,2])

#Print first row
print("First row:")
print(matrix[0,:])

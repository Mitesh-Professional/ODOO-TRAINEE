import numpy as np

# matrix in numpy array

matrix_value_1 = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(matrix_value_1)
print(f"Shape Of a Project:- {matrix_value_1.shape[0]}x{matrix_value_1.shape[1]}")
print(type(matrix_value_1))
print()
matrix_value_2 = np.matrix([[11, 12, 13], [14, 15, 16], [17, 18, 19]])

print(matrix_value_2)
print(f"Shape Of a Project:- {matrix_value_2.shape[0]}x{matrix_value_2.shape[1]}")
print(type(matrix_value_2))

print(f"Addition of Matrix:-")
print(matrix_value_1 + matrix_value_2)
print()
print(f"Multiplication of Matrix:-")
# Also called Dot Multiplication
print(matrix_value_1 * matrix_value_2)
print(matrix_value_1.dot(matrix_value_2))

# Matrix function in numpy
# 1. Transpose
# 2. Swapaxes
# 3. inverse
# 4. Power
# 5. Determinate
print()
matrix_value_3 = np.matrix([[1, 2, 3], [4, 5, 6]])
print(matrix_value_3)
print()
print(f" Transpose of Matrix:- ")
print(np.transpose(matrix_value_3))
print("Short Trick:-")
print(matrix_value_3.T)
print()

print(f'Swapaxes:-')
print(np.swapaxes(matrix_value_3, 0, 1))
print()

matrix_square = np.matrix([[1, 2], [3, 4]])
print(matrix_square)
print("This is Square Matrix")
print(np.swapaxes(matrix_square, 0, 1))

# Inverse Matrix

print("This Inverfinal_listse Matrix of a")
print(matrix_square)
# linalg.inv this is function for finding a value of inverse of matrix
print("Inverse Matrix = ")
print(np.linalg.inv(matrix_square))

# Power Of Matrix value

print("this is normal matrix")
print(matrix_square)

# there is three type of N are available for a Conversion
# when you are pass parameter for power. it's take three parameter
# n<0 n>0 n=0flatten

print("Normal matrix:-")
print(matrix_square)
print()

print("Power of matrix value")
print("This is n>0 Matrix")
print(np.linalg.matrix_power(matrix_square,2))
print()

print("This is n=0 Matrix")
print(np.linalg.matrix_power(matrix_square,0))
print()

print("This is 0<n Matrix")
print(np.linalg.matrix_power(matrix_square,-2))

print("Matrix Determinate")
print()

print(np.linalg.det(matrix_square))

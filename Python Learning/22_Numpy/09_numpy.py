# Shape and Reshaping in Numpy Array
import numpy as np


var = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(var.shape)


var2 = np.array([1,2,3],ndmin=4)
print(var2.shape)


# first = number of column c/r
# second = number of row
#  This for Two args

# print(var.reshape(1,5))

var3 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(var3.reshape(3,2))
print(var.reshape(2,6))

# if given three args so your want change parameter
# number of rows -
# number of rows data |
# number of columns

print(var3.reshape(2,3,2))
print(var.reshape(3,2,2))



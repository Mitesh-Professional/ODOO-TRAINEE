import numpy as np

# Broadcasting Numpy Array

var_1 = np.array([1,2,3])
var_2 = np.array([[1], [2], [3], [4]])
print(var_1)
print(var_1.shape)
print(var_2)
print(var_2.shape)

print(var_1+var_2)

#      1   2   3
#
#  1   2   3   4
#  2   3   4   5
#  3   4   5   6
#  4   5   6   7

# 2x1 2x3 done we have one and also have 2


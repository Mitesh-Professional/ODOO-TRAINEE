# Arithmatic operation in numpy array
import numpy as np

var = np.array([1, 2, 3, 4])
var2 = np.array([5, 6, 7, 8])
var_add = var + var2
print(var_add)

var_sub= var - var2
print(var_sub)

var_multi = var * var2
print(var_multi)

var_div = var / var2
print(var_div)

var_power = var ** var2
print(var_power)

var_add = var % var2
print(var_add)

# 2D Array
two_d_array = np.array([[1, 2, 3, 4],[5, 6, 7, 8]])
two_d2_array = np.array([[1, 2, 3, 4],[5, 6, 7, 8]])
three_d_array = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])
print(two_d_array)
print(two_d_array % 2)
print(var+two_d_array)
print(two_d_array+two_d2_array)
# print(three_d_array + two_d_array)




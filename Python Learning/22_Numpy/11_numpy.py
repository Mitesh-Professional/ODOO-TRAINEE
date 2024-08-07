# indexing And Slicing in Numpy Array
import numpy as np

var_1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(var_1[-1])
var_2 = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
print(var_2[-1][0])
print(var_1[0:6])
print(var_1[0:5:3])
print(var_1[::-1])
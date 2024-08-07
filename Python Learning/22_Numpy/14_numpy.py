import numpy as np

# join and split function in numpy array

# Join Array
var_1 = np.array([1,2,3,4])
var_2 = np.array([5,6,7,8])
concat_value = np.concatenate((var_1,var_2))
print(concat_value)


var_3 = np.array([[1,2], [3,4]])
var_4 = np.array([[5,6], [7,8]])

concat_value_2 = np.concatenate((var_3,var_4),axis=1)
print(concat_value_2)

# Stack Method
# hstack
# vstack
# dstack height
stack_value = np.vstack((var_1,var_2))
print(stack_value)

# Split function

var_5 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
split_array = np.array_split(var_5, 5)
print(split_array)
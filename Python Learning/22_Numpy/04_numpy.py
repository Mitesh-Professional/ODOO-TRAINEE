import numpy as np

# create numpy array using numpy function

# array filled by 0's
zero_value_array = np.zeros(4)
zero_dimension_array = np.zeros((4,4))
print(zero_value_array)
print(zero_dimension_array)

# array filled by 1's
one_value_array = np.ones(4)
print(one_value_array)

# Create an empty
# it's Showing previous data stored in memory
empty_array = np.empty(4)
print(empty_array)

# An Array with range of element
range_array = np.arange(4)
print(range_array)

# array diagonal element filled with 1's
diagonal_array = np.eye(4)
print(diagonal_array)
# Create an array with value that are spaced linearly in specified Interval

spaced_linearly_array = np.linspace(0, 10, num=5)
print(spaced_linearly_array)


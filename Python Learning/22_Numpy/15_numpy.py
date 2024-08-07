import numpy as np

# Numpy Functions (Search, sort, Search Sorted, Filter)

var = np.array([1, 2, 3, 4, 5, 2, 3, 1, 8, 4, 1])
print(var)

# Search
search_value = np.where(var == 1)
print(search_value)

# Search Sorted
# this move left to right
# if you want change oder of search change if you can
# use Keyword is side="left or right"
var_1 = np.array([1, 3, 4, 5])
#                 3  2  1  0 right
#                 0  1  2  3 left
x_1 = var_1.searchsorted(2, side="right")
print(x_1)
# Error

# Sort Array

random_array = np.array([9,3,5,4,1,8,7,6,2])
x = np.sort(random_array)
print(x)

# sort in 2D array

two_d_array = np.array([[9,7,8],[2,1,3],[6,4,5]])
two_d_array_sort = np.sort(two_d_array)
print(two_d_array_sort)

# Filter Function in numpy array
print(x)
filter_arr = [True, False, False, False, False, False, False, False, True]
filter_value = x[filter_arr]
print(filter_value)

import numpy as np

# numpy array functions

# Shuffle
# unique
# Resize
# Flatten
# Ravel

# Shuffle Numpy Array

shuffle_array = np.array([1,2,3,4,5,6])
np.random.shuffle(shuffle_array)
print(shuffle_array)

# Unique Data Find in Numpy Array

unique_array = np.array([1,2,2,4,5,3,4,5,1,5])
unique_value = np.unique(unique_array,True, return_counts=True)
print(unique_value)

# Resize of Numpy Array

resize_array = np.array([1,2,3,4])
# resize taken Two args 1 row 2 columns
resize_array.resize((4, 1))
print(resize_array)
print()
# Flatten a array

array_for_flatten = np.array([[1,2,3], [4, 5, 6]])
print(array_for_flatten)
print()
# flatten have some of oder {C,F,A,K}
# Default have C
# Read line by Line
# F = [1 2 3]
#     [4 5 6]
# Read column type 14, 25, 36
print(array_for_flatten.flatten('F'))

# A = [1 2 3]
#     [4 5 6]
print(array_for_flatten.flatten("A"))

# A = [1 2 3]
#     [4 5 6]
print(array_for_flatten.flatten("K"))

# Ravel in numpy Array

print(array_for_flatten.ravel("F"))

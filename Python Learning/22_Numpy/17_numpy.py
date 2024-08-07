import numpy as np

# Numpy Array function insert and delete

array_number = np.array([1, 2, 3, 4, 5])
# First is Array Name
# Second is index
# third is value of you want insert
new_array = np.insert(array_number, 3, 500)
print(new_array)

new_array = np.insert(array_number, (1, 4), 500)
print(new_array)

# Float value can't Assign only you can assign Integer value
new_array = np.insert(array_number, 3, 4.10)
print(new_array)
print()

two_d_array = np.array([[1, 2, 3], [4, 5, 6], [6, 7, 8]])
print(two_d_array)

new_array = np.insert(two_d_array, 2, [11, 12, 13], 1)
print(new_array)
print()

# Append Method in numpy array

array_number = np.array([1, 2, 3, 4, 5])
x = np.append(array_number, 8.6)
print(x)

x = np.append(two_d_array, [[12, 23, 34]], axis=0)
print(x)

# Delete method in numpy array

array_number = np.array([1, 2, 3, 4, 5])
print(array_number)
x = np.delete(array_number, 2)
print(x)

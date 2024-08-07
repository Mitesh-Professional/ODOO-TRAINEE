import numpy as np

# two way to create array

numpy_array = np.array([1, 2, 3, 4])
print(numpy_array)
print(type(numpy_array))


list_number = []

# for i in range(0,4):
#     user_value = int(input("Enter your number:- "))
#     list_number.append(user_value)
#
# new_array = np.array(list_number)
# print(new_array)

print(f"Showing Dimension of Array :- {numpy_array.ndim}")


# Create Two Dimension of Data
# Carefully Understand when you create multi Dimension Array so make sure you All data length are equal.

multi_dimension_data = np.array([[1, 2, 3], [4, 5, 6]])

print(multi_dimension_data)
print(f"Showing Dimension of Array :- {multi_dimension_data.ndim}")


multi_dimension_data = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])

print(multi_dimension_data)
print(f"Showing Dimension of Array :- {multi_dimension_data.ndim}")

# ndmin = this is created dimensions

multi_dimension_data = np.array([1, 2, 3], ndmin=10)

print(multi_dimension_data)
print(f"Showing Dimension of Array :- {multi_dimension_data.ndim}")




# Sliceing use for All intrable Object

list_value = [1,2,3,4,5]
str_value = "Mitesh"
tuple_value = (1,2,3,4,5)
print("\n")
# Basic Slicing
print("Basic Slicing")
print(list_value[1:4])
print(str_value[0:2])
print(tuple_value[:])
print("\n")

# Step Value
print("Step Value Slicing")
print(list_value[:5:2])
print(str_value[0:4:3])
print(tuple_value[::2])
print("\n")

# Negative Indices
# Negative Indices Calculating using this method
#len(x)-1
print("Negative Indices")
print(list_value[:-1])
print(str_value[-6:-2])
print(tuple_value[-4:-1])
print("\n")

# Revers Slicing
print("Revers Slicing")
print(list_value[::-1])
print(str_value[1::-1])
print(tuple_value[:-3:-1])




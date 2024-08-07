# Simple Lambda Functions
squre_of_num = lambda x: x ** 2

print(squre_of_num(8))


# Argument With Lambda Function

sum_num = lambda x,y: x+y
print(sum_num(10,20))

# using Lambda with a Map function

list_of_number = [1,2,3,4,5,6,7,8,9]
print(list_of_number)
squre_of_list = list(map((lambda x: x**2),list_of_number))
print(squre_of_list)


# Using Lambda Function With a filter Function

find_even_number_in_list = list(filter((lambda x: x % 2 == 0), list_of_number))
print(find_even_number_in_list)

# Function inside another function

def my_func(n):
    return lambda x: x * n
dubble_value = my_func(2)

print(dubble_value(2))
list_of_number = [1,2,3,4,5,6,7,8,9,10]

map_function = map((lambda x: x**2),list_of_number)
print(map_function)
print(list(map_function))

filter_function = filter((lambda x: x>5),list_of_number)
print(filter_function)
print(list(filter_function))
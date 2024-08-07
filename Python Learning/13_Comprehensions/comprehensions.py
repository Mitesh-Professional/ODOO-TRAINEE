# Comprehensions

create_new_list_using_comprehensions = [x for x in range(1,101)]

print("This List make by comprehension method:- ", create_new_list_using_comprehensions)

odd_number_list = [x for x in create_new_list_using_comprehensions if x % 2 != 0]
print("Odd List:- ",odd_number_list)

list_of_keys = ["name","age","gender",'experience']
list_of_values = ['mitesh', '0', 'male', '0.1']
dic_create_using_comprehension = {k: v for k,v in zip(list_of_keys,list_of_values)}
print(dic_create_using_comprehension)


# Creating a Dictionary with Expressions

dic_create_using_expressions = {x: x**2 for x in range(0,11)}
print(dic_create_using_expressions)


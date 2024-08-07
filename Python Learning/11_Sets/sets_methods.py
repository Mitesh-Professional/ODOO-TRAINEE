# Sets Methods

user_sets = {2, 3, 4, 5, 6}
user_sets.add(7)
print(user_sets)

user_sets.remove(4)
print(user_sets)

user_sets.clear()
print(user_sets)

user_sets = {2, 3, 4, 5, 6}
print(len(user_sets))

if 5 in user_sets:
    print("Yes")


set_a = {1, 2}
set_b = {2, 3, 4}

union_of_set = set_a | set_b
print(user_sets)

intersection_of_set = set_a & set_b
print(intersection_of_set)

difference_of_set = set_a - set_b
print(difference_of_set)

symmetric_difference = set_a ^ set_b
print(symmetric_difference)

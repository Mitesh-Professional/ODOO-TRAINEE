# Tuple Methods

tuple_items = (1, 1, 2, 3, 4, 5, 6)
print("This is Default Tuple:- ",tuple_items)

tuple_value = tuple_items.count(1)

print("Tuple Count Method:- ", tuple_value)

tuple_value = tuple_items.index(4)
print("Tuple Index Method:- ",tuple_value)

tuple_value = len(tuple_items)
print("Tuple Len Method:- ", tuple_value)

tuple_value = max(tuple_items)
print("Tuple Max Methods",tuple_value)

tuple_value = min(tuple_items)
print("Tuple Min Methods",tuple_value)

tuple_value = sum(tuple_items)
print("Tuple Sum Methods",tuple_value)

new_tuple_items = (2, 1, 5, 4, 6, 3, 9, 7, 8)
tuple_value = sorted(new_tuple_items)
print("Tuple Max Methods",tuple_value)

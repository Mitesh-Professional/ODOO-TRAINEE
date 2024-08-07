dic_items = {'name': ['mitesh', 'raj', 'smith', 'raja', 'rani'], 'age': [1, 2, 3, 4, 5, 6]}

print("this is a real Dictionary :-", dic_items)

# clear()

dic_items.clear()
print('Clear() Methods Answer :-', dic_items)

dic_items = {'name': ['mitesh', 'raj', 'smith', 'raja', 'rani'], 'age': [1, 2, 3, 4, 5, 6]}

# copy()
new_dic = dic_items.copy()
print('Copy() Methods Answer :-', new_dic)
print('Checking Both Dic using == :-', dic_items == new_dic)
print('Checking Both Dic using is :-', dic_items is new_dic)

# fromkeys()

create_new_dic_using_fromkeys = dic_items.fromkeys(["name",'age','value','date'],['mitesh',1,'20k taken','2023'])
print('Fromkeys() Methods Answer :-', create_new_dic_using_fromkeys)

# get(key)

find_value_using_get = dic_items.get('name')
print('Get() Methods Answer :-', find_value_using_get)

# items()Get

item_value = dic_items.items()
print('Items() Methods Answer :-', item_value)

# keys()

keys_to_find_keys = dic_items.keys()
print('Keys() Methods Answer :-', keys_to_find_keys)

# pop(key)

pop_key = dic_items.pop('name')
print('Pop() Methods Answer :-', pop_key)
print(dic_items)

dic_items = {'name': ['mitesh', 'raj', 'smith', 'raja', 'rani'], 'age': [1, 2, 3, 4, 5, 6]}

# values()

dictionary_values = dic_items.values()
print('Values() Methods Answer :-', dictionary_values)
print(dictionary_values)

# SetDefault()

set_default_dictionary = {}
set_default_dictionary.setdefault('Name', 'Enter Your Name')
print('setdefault() Methods Answer :-',  set_default_dictionary)

# Update()

dic_items.update({'age': [1,2,3,4,5,6,7]})
print('Update() Methods Answer :-', dic_items)

# popitem()

pop_item = dic_items.popitem()
print('PopItem() Methods Answer :-', dic_items)
print("Pop Item Is :-", pop_item)




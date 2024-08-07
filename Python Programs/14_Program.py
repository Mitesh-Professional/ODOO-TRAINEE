from collections import defaultdict

default_dic = defaultdict(list)
test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]
print(test_list)
result = []

for key,value in  test_list:
    default_dic[key].append(value)

for key,value in default_dic.items():
    result = [(key, *value) for key,value in default_dic.items()]
print(result)
test_string = "GeeksforGeeks is best"
length = len(test_string)/7
list_value = []
staring = 0
count = 1
for index in range(0, int(length)):
    value = 7 * count
    new_str = test_string[staring: value]
    new_list = []
    for str in new_str:
        new_list.append(str)
    list_value.append(new_list)
    count += 1
    staring = value

print(list_value)


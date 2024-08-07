import numpy as np

list_str = input().split(' ')
matrix_info = list(map(int, list_str))
final_list = []
for i in range(0, matrix_info[0]):
    inp = input().split(' ')
    int_list = list(map(int, inp))
    final_list.append(int_list)

np_array = np.array(final_list, float)

print(np.mean(np_array, 1))
print(np.var(np_array, 0))
print(np.std(np_array, None))

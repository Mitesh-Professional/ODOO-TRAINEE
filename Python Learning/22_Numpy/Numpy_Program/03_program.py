import numpy as np

list_str = input().split(' ')
matrix_info = list(map(int,list_str))
final_list = []
for i in range(0,matrix_info[0]):
    inp = input().split(' ')
    int_list = list(map(int,inp))
    final_list.append(int_list)

np_array = np.array(final_list)
np_sum = np.sum(np_array,axis = 0)
np_prod = np.prod(np_sum)
print(np_prod)

# The first line of input contains space separated values of N and M.
# The next N lines contains M space separated integers.
# 2 2
# 1 2
# 3 4

# 24
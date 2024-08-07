import numpy as np

input_value_0 = input().split(' ')
matrix_len_value = list(map(int,input_value_0))
final_list = []
for i in range(0,2):
    inner_list = []
    for j in range(0,matrix_len_value[0]):
        input_value = input().split(' ')
        inner_list.append(list(map(int,input_value)))
    final_list.append(inner_list)
print(np.add(final_list[0],final_list[1]))
print(np.subtract(final_list[0],final_list[1]))
print(np.multiply(final_list[0],final_list[1]))
print(np.floor_divide(final_list[0],final_list[1]))
print(np.mod(final_list[0],final_list[1]))
print(np.power(final_list[0],final_list[1]))


# 1 4
# 1 2 3 4
# 5 6 7 8

# [[ 6  8 10 12]]
# [[-4 -4 -4 -4]]
# [[ 5 12 21 32]]
# [[0 0 0 0]]
# [[1 2 3 4]]
# [[    1    64  2187 65536]]

# 2 4
# 1 2 3 4
# 1 2 3 4
# 5 6 7 7
# 5 6 7 7

# [[ 6  8 10 11]
#  [ 6  8 10 11]]
# [[-4 -4 -4 -3]
#  [-4 -4 -4 -3]]
# [[ 5 12 21 28]
#  [ 5 12 21 28]]
# [[0 0 0 0]
#  [0 0 0 0]]
# [[1 2 3 4]
#  [1 2 3 4]]
# [[    1    64  2187 16384]
#  [    1    64  2187 16384]]
import numpy as np
np.set_printoptions(legacy='1.13')
list_value = input().split(' ')
int_list = list(map(float,list_value))

np_array = np.array(int_list)
print(np.floor(np_array))
print(np.ceil(np_array))
print(np.rint(np_array))


# 1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9

# [1. 2. 3. 4. 5. 6. 7. 8. 9.]
# [ 2.  3.  4.  5.  6.  7.  8.  9. 10.]
# [ 1.  2.  3.  4.  6.  7.  8.  9. 10.]
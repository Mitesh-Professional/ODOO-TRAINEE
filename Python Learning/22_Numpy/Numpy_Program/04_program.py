import numpy as np

rows, cols = map(int, input().split())

matrix = []
for _ in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)
np_array = np.array(matrix)
np_min = np.min(np_array,1)
print(np.max(np_min))


# 4 2
# 2 5
# 3 7
# 1 3
# 4 0


# 3

# You are given a 2-D array with dimensions NxM.
# Your task is to perform the min function over axis 1 and then find the max of that.
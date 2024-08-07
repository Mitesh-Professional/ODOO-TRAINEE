# iterating in numpy array
import numpy as np

var = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]])

for i in var:
    for j in i:
        for k in j:
            print(k)
print("___________")
print("nditer Method For Iterate Numpy Array")
print("___________")
for i in np.nditer(var):
    print(i)

print("___________")
print("Change Dtype of Variable")
for i in np.nditer(var,flags=['buffered'],op_dtypes=['S']):
    print(i)

print("___________")
for i,v in np.ndenumerate(var):
    print(i,v)

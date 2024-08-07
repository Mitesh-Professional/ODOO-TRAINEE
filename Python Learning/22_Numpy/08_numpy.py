# Arithmatic Function in Numpy Array

import numpy as np

var = np.array([1,2,3,4])
new_value = var.max()
print(new_value)
print("Max:- ", np.max(var))
print("Min:- ", np.min(var))
print("Argmin:- ", np.argmin(var))
print("Argmax:- ", np.argmax(var))
print("Square root:- ", np.sqrt(var))
print("Sin:- ", np.sin(var))
print("Cos:- ", np.cos(var))
print("Cumsum:- ",np.cumsum(var))

var = np.array([[1,2,3,4],[5,6,7,8]])
print(np.min(var,axis=1))
print(np.max(var, axis=1))

print(np.min(var,axis=0))
print(np.max(var, axis=0))


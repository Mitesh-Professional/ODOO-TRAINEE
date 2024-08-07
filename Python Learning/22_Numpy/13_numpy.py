# Copy Vs View in Numpy array
import numpy as np

var = np.array([1,2,3,4])
copy_data = var.copy()

print("Var:- ", var)
print("Copy Data:- ", copy_data)
var[1] = 20
print("Change Data From Main var")
print("Var:- ", var)
print("Copy Data:- ", copy_data)

x = np.array([1,3,4,5,6])
vi = x.view()
print("X:- ", x)
print("View Data:- ", copy_data)
x[0] = 1000
print("Change Data From Main var")

print("X:- ", x)
print("View Data:- ", vi)

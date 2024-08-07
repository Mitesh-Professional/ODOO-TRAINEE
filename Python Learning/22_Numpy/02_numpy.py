import numpy as np
import timeit

arr = np.arange(5)
squared_arr = arr**2

def square_elements():
    return arr**2

# Measure the execution time
time_taken = timeit.timeit(square_elements, number=100000)

print("Squared array:", squared_arr)
print(f"Time taken: {time_taken:.6f} seconds")

my_list = [1, 2, 3, 4, 5]

def square_elements(lst):
    return [x**2 for x in lst]

# Measure the execution time
time_taken = timeit.timeit(lambda: square_elements(my_list), number=100000)

print("Squared list:", square_elements(my_list))
print(f"Time taken: {time_taken:.6f} seconds")

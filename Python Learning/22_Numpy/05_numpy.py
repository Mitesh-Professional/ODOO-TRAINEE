import numpy as np

# Create numpy array using Random number

# Rand Function given value 0 and 1 between

rand_array = np.random.rand(4)
print("Single Dimension:- ", rand_array)
print()

rand_array = np.random.rand(2,4)
print("Multi Dimension:- ", rand_array)
print()

# Randn Function This is Generate value close to Zero Also given number is Positive or Negative
randn_array = np.random.randn(2)
print("Single Dimension:- ", randn_array)
print()

randn_array = np.random.randn(3,2)
print("Multi Dimension:- ", randn_array)
print()

# Ranf this generates 0.0 to 1.0 but 1 is not included and also this given in float format

ranf_array = np.random.ranf(3)
print("Single Dimension:- ", ranf_array)
print()

# Randint generates number between given range

randint_array = np.random.randint(0,10,4)
print(randint_array)
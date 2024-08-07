# Map Function
* The map function applies a given function to all items in an input list (or any iterable) and returns a map object (which is an iterator). 
* Syntax:
* map(function, iterable)
* Example:
* Function to double the value 
* def double(n):
* return n * 2 
* numbers = [1, 2, 3, 4]
* result = map(double, numbers)
* print(list(result))  # Output: [2, 4, 6, 8]
# Filter Function
* The filter function constructs an iterator from elements of an iterable for which a function returns true. 
* Syntax:
* filter(function, iterable)
* Example:- 
* Function to check if a number is even
* def is_even(n):
* return n % 2 == 0 
* numbers = [1, 2, 3, 4, 5, 6]
* result = filter(is_even, numbers)
* print(list(result))  # Output: [2, 4, 6]


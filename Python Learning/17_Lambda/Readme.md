# Lambda Functions:-

* Lambda functions in Python are small, anonymous functions defined with the lambda keyword. They can take any number of arguments but can only have one expression. Here’s a quick overview with examples:
## Basic Syntax
* The syntax for a lambda function is:
* lambda arguments: expression

## Example 1: Simple Lambda Function:-
* Here’s a simple example that adds 10 to a given number:
* add_ten = lambda x: x + 10 
* print(add_ten(5))  # Output: 15

## Example 2: Lambda with Multiple Arguments
* You can also create lambda functions with multiple arguments:
* multiply = lambda x, y: x * y 
* print(multiply(5, 6))  # Output: 30

## Example 3: Using Lambda with map()
* Lambda functions are often used with functions like map(), filter(), and reduce(). Here’s an example using map() to square each number in a list:
* numbers = [1, 2, 3, 4, 5]
* squared_numbers = list(map(lambda x: x**2, numbers))
* print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

## Example 4: Using Lambda with filter()
* You can use filter() to filter out elements from a list based on a condition:
* numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
* even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
* print(even_numbers)  # Output: [2, 4, 6, 8, 10]

## Example 5: Lambda Inside Another Function
* Lambda functions can also be used inside other functions:
* def myfunc(n):
* return lambda a: a * n 
* doubler = myfunc(2)
* print(doubler(11))  # Output: 22 
* tripler = myfunc(3)
* print(tripler(11))  # Output: 33


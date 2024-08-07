# Functions:-

* A function is a named block of code that performs a specific task or returns a value.
* You define a function using the def keyword, followed by the function name and a set of parentheses.
* def greet():
*   print("Hello, world!")
* Call the function
* greet()
* Output: Hello, world!

## Parameters and Arguments:
* Functions can accept parameters (also known as arguments).
* Parameters are variables listed inside the parentheses in the function definition.
* Arguments are the actual values passed to the function when it is called.
* Example with a parameter:
* def greet(name):
* print(f"Hello, {name}!")
* greet("Alice")  # Argument: "Alice"
* Output: Hello, Alice!

## Returning Values:
* A function can return a value using the return statement.
* Example:
* def add(a, b):
*   return a + b 
* result = add(3, 5)
* print("Sum:", result)
* Output: Sum: 8

## Keyword Arguments:
* You can pass arguments using the key-value syntax.
* Order doesn’t matter for keyword arguments.
* Example:
* def describe_person(name, age):
* print(f"{name} is {age} years old.")
* describe_person(age=30, name="Bob")
* Output: Bob is 30 years old.
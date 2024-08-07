# F-String:-
*  f-strings (formatted string literals) in Python provide a concise and readable way to embed expressions inside string literals. Introduced in Python 3.6, they are prefixed with an f or F and use curly braces {} to evaluate expressions.
* Here’s a basic example:
* name = "Alice"
* age = 30 
* print(f"Hello, my name is {name} and I am {age} years old.")
* This will output:
* Hello, my name is Alice and I am 30 years old.

# Key Features of f-strings:
## Variable Interpolation: Directly embed variables within strings.
## Expression Evaluation: Perform calculations or call functions inside the curly braces.
## Formatting: Use format specifiers to control the appearance of the output.
## Example with Expressions:
* a = 5 
* b = 10 
* print(f"The sum of {a} and {b} is {a + b}.")
* This will output:
* The sum of 5 and 10 is 15.
## Example with Formatting:

* value = 123.456 
* print(f"Formatted value: {value:.2f}")
* This will output:
* Formatted value: 123.46

# Advantages of f-strings:
## Readability: More readable and concise compared to older methods like % formatting or str.format().
## Performance: Generally faster than other string formatting methods
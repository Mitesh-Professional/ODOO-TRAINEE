# Raising Exceptions:-
* To raise an exception, you use the raise statement. This is useful when you want to signal that an error has occurred. For example:
* def divide(x, y):
* if y == 0:
* raise ValueError("Cannot divide by zero!")
* return x / y
* try:
* result = divide(10, 0)
* except ValueError as e:
* print(e)

# Handling Exceptions:-

* To handle exceptions, you use the try and except blocks. This allows you to catch and manage errors gracefully:
* try:
* result = divide(10, 2)
* print(result)
* except ValueError as e:
* print(f"Error: {e}")

## You can also use else and finally blocks for additional control:
* try:
* result = divide(10, 2)
* except ValueError as e:
* print(f"Error: {e}")
* else:
* print(f"Result is {result}")
* finally:
* print("Execution completed.")

## else: Executes if no exceptions are raised.
## finally: Executes regardless of whether an exception was raised or not.

# Custom Exceptions:-
* You can define your own exceptions by creating a new class derived from the built-in Exception class:
* class CustomError(Exception):
* pass
* def check_value(value):
* if value < 0:
* raise CustomError("Negative value not allowed!")
* try:
* check_value(-1)
* except CustomError as e:
* print(e)

# Best Practices:-
* Be specific: Raise specific exceptions to make error handling easier.
* Use meaningful messages: Provide clear and informative error messages.
* Avoid using exceptions for control flow: Use exceptions for error handling, not for regular control flow.


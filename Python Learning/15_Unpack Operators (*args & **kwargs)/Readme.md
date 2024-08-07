# Unpack Operators (*args, **kwargs)
* *args (Non-Keyword Arguments):
* The special syntax *args in function definitions allows you to pass a variable number of non-keyworded arguments to a function.
* It collects these arguments into a tuple.
* Example:
* def myFun(*argv):
* for arg in argv:
* print(arg)
* myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')
* Hello 
* Welcome
* to 
* GeeksforGeeks

## **kwargs (Keyword Arguments):
* The special syntax **kwargs in function definitions allows you to pass a keyworded, variable-length argument list.
* It collects these arguments into a dictionary.
* Example:
* def greet(**kwargs):
* for key, value in kwargs.items():
* print(f'{key}: {value}')
* greet(first='Geeks', second='for', third='Geeks')
* first: Geeks
* second: for
* third: Geeks




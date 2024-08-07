# Functions

def functions_create():
    print("Hello, My Name is a Mitesh.");

functions_create()

# Parameters and Arguments
def parameters_functions(name):
    print("Your Name is ",name)

parameters_functions("mitesh")

# Returning Values:

def squre_return(number):
    return number ** 2

print(squre_return(3))


# Keyword Arguments:

def keyword_function(name,age):
    print(f"you name is a {name}. and your age is {age}.")

keyword_function(age=10,name="mitesh")
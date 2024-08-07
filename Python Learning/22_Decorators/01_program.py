def toll(func):
    def wrapper():
        print(f"Your Function Name is:- {func.__name__}")
        result = func()
        print("You Have Good day.")
        return result
    return wrapper

@toll
def good_morning():
    print("Hello sir, Good Morning!!!")

good_morning()
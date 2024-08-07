def deco(func):
    def wrapper(*args):
        result = func(*args)
        print(f"I am Mediater of Both Func. Your Name is {func.__name__}")
        return result
    return wrapper

@deco
def test_func(n):
    print("Value is:- ",n)

test_func(4)

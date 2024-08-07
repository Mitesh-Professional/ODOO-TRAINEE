import time

def cache(func):
    cash_value = {}
    print(cash_value)
    def wrapper(*args, **kwargs):
        if args in cash_value:
            return cash_value[args]
        result = func(*args, **kwargs)
        cash_value[args] = result
        return result
    return wrapper
@cache
def time_func(a,b):
    time.sleep(4)
    return a + b
print(time_func(2,2))
print(time_func(2,2))

# what is behind logic

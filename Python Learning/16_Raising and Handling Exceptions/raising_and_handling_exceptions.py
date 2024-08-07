def rising_error(i):
    try:
        b = i /0
        print(b)
    except ZeroDivisionError as e:
        print(e)
# user_value = int(input("Enter Your Value"))
user_value = 12
rising_error(user_value)


# raising Custom Error

try:
    a = 0
    if a == 0:
        raise ValueError("Your Value is Zero!!!")
except ValueError as e:
    print(e)
finally:
    print("It's Run All The Time")


def exceptions_handling(i):
    try:
        if type(i) == str:
            raise ArithmeticError("Your Value is Str!!")
        else:
            print(i+1)
    except ArithmeticError as e:
        print(e)
    else:
        print("All Case Are Fail!")
    finally:
        print("this is run All the Time!")
exceptions_handling(True)
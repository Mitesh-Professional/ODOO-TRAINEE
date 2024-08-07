from deco import Session

user_status = False
# print(Session.__call__.__doc__)
@Session
def user_open_web(bool_value):
    print("Website Start!")

user_open_web(user_status)
# conditional operation:-


# If Statement:-

# user_input = int(input("Enter Your Age is :- "))
user_input = 20
if user_input>= 18:
    print("You can Vote!!!!!!!!!!")

# If-Else Statement

if user_input > 30:
    print("you are mature")
else:
    print("You are Adult")

# Nested If-Else Statement
value_of_user = "mitesh"
if value_of_user != "mitesh":
    print(False)
else:
    if value_of_user == 'mitesh':
        print("Hello, Welcome Mitesh!!!!!!!!!!!")
    else:
        print("You Are not Mitesh!")
# If-Elif-Else Statement
user_conditional_value= 2
if user_conditional_value <= 5:
    print("you are Kids")
elif user_conditional_value<=17:
    print("You are Children")
elif user_conditional_value >= 18:
    print("You are elder")
# Ternary Expression

user_auth = "Mitesh"
auth = "Member of This Company!!!!!!!!!" if user_auth == "Mitesh" else print("You Are not Auth Person")
print(auth)

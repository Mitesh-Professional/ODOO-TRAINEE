import random

print("Welcome to My Game:- ")
print("Game Name is Guess The Number")

system_number = random.randint(1,1000)
# print(system_number)
while True:
    user_input = int(input("Enter Your Guess Number:- "))
    if(user_input == system_number):
        print("You Are Won!!!!!")
        print("System Number Is a:- ",system_number)
        break
    elif user_input < system_number:
        print("Your Number is an Vary Small!!")
    elif user_input > system_number:
        print("Your Number is an Vary High!!!")
    else:
        print("Check Your Guess!!!!!!!!!")
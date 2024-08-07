# 02 program to check armstrong number

userInput = input("Enter Your Number To Check Armstrong or Not:- ")

def check_armstrong_number(number):
    sum = 0
    for i in number:
        num = int(i)
        value = num**3
        sum += value
    num = int(number)
    if num == sum:
        return "Armstrong Number!"
    else:
        return "this is not Armstrong number!"
print(check_armstrong_number(userInput))

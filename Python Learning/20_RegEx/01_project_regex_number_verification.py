# Verification Number
import re

# number = input("Enter Your Mobile NUmber:- ")

num = "111-111-11111"
if re.search(r"\d{3}-\d{3}-\d{4}", num):
    print("Number is Correct!")
else:
    print("You Number is Not Right Format")

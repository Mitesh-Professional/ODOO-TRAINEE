def palindrome_number(number_string):
    str_new = number_string[::-1]
    if number_string == str_new:
        return "This is Palindrome String."
    else:
        return "This not Palindrome String."

user_entred_data = input("Enter Your Number to Check for Number is Palindrome or Not:- ")

print(palindrome_number(user_entred_data))
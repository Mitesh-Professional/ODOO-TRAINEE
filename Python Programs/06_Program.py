def checking_number_is_odd_or_even(number):
    new_number = number/2
    cover_int = int(new_number)
    if new_number == cover_int:
        return "Even"
    else:
        return "Odd"

print(checking_number_is_odd_or_even(17))

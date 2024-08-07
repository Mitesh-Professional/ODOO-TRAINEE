#program to print all prime number in Interval

def prime_number_check(start,end):
    list = []
    for i in range(start,end):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                list.append(i)
    return list

user_staring_number = int(input("Enter Your Staring Number:- "))
user_ending_number = int(input("Enter Your Ending Number:- "))

print(prime_number_check(user_staring_number,user_ending_number))

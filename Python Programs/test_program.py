11) Python program to extract only the numbers 
from a list which have some specific digits using Using filter() + lambda 
Input : test_list = [3456, 23, 128, 235, 982], dig_list = [2, 3, 5, 4] 
Output : [23, 235]

# 12) Extract tuples having K digit elements using map fuction
# Input : test_list = [(54, 2), (34, 55), (222, 23), (12, 45), (78, )], K = 2
# Output : [(34, 55), (12, 45), (78,)]

# int(ele) in dig_list for ele in str(sub)

list_of_tuple = [(54, 2), (34, 55), (222, 23), (12, 45), (78, )]
list_result = []
for tup in list_of_tuple:
    nub = len(tup)
    print(nub)
    tup_new = []
    for i in range(0,nub):
        str_number = len(str(tup[i]))

        if str_number == 2:
            tup_new.append(tup[i])
        else:
            tup_new = []
            break
    if not tup_new:
        del tup_new
    else:
        tup_covert = tuple(tup_new)
        list_result.append(tup_covert)
print("next tup",list_result)

import itertools

def all_combinations(input_string):
    length = len(input_string)
    combinations = [''.join(p) for p in itertools.product(input_string, repeat=length)]
    return combinations

input_string = 'abc'
print(all_combinations(input_string))

def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number+1):
        deci = str(i)
        octa = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        bina = bin(i)[2:]
        print(deci.rjust(width),octa.rjust(width),hexa.rjust(width),bina.rjust(width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


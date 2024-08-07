# program to print fibonacci sequence
def fibonacci_sequence(number_of_series):
    # checking phase
    if number_of_series == 1 or number_of_series == 0:
        return [0,1]
    else:
        list = [0,1]
        for i in range(0,number_of_series):
            new_list = list[i]+list[i+1]
            list.append(new_list)
            # print(new_list)
        return list
print(fibonacci_sequence(10))


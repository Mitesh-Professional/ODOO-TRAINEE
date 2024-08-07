def fibonacci_sequence(number):
    if number == 0:
        return [0]
    elif number == 1:
        return [0,1]
    else:
        list_of_result = []
        for i in range(0, number):
            if len(list_of_result)<2:
                list_of_result.append(i)
            else:
                new_list = int(list_of_result[i-1]) + int(list_of_result[i-2])
                list_of_result.append(new_list)
        return list_of_result

print(fibonacci_sequence(10))
def specific_digits(num_list, dig_list):
    return list(filter(lambda x: all(int(e) in dig_list for e in str(x)), num_list))

test_list = [3456, 23, 128, 235, 982]
dig_list = [2, 3, 5, 4]
result = specific_digits(test_list, dig_list)
print("Extracted elements:", result)
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

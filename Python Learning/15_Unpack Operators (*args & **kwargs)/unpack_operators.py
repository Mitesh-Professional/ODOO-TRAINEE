def create_list(*args):
    list_value = []
    for x in args:
        list_value.append(x)
    return list_value

print(create_list(1, 2, 3, 4, 5))

def create_dic(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}: {v}")

create_dic(name= "mitesh",age=0,exprience = 0.1)
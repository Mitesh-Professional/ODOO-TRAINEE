# Pandas DataFrame

import pandas as pd

list_of_number = [1,2,3,4,5,6,7]
dt = pd.DataFrame(list_of_number)
print("This DataFrame:-")
print(dt)
print(type(dt))


dic = {"a":[1,2,3,4],
       "s":[5,6,7,8]}
dt1 = pd.DataFrame(dic)
print(dt1)
# this most Important part in a Dataframe
# when we pass data in dataframe and data is dictionary so you have carefully dic data size same as example
# else you got error but you shoud be remebar this part.
# also find value of one line so you want pass columns=["name of columns"]
# if you want to many columns so you can give coma sapreted value example = ["a",1]
# also we can change index using index keyword
print("This is Columns Part")
dt2 = pd.DataFrame(dic,columns=["a"])
print(dt2)


# Data get in data frame

print(dt1)
print(dt1["s"][2])

# create dataframe using list

list_of_item = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
df = pd.DataFrame(list_of_item)
print(df)


# when combination of two or more list and series make dataframe
# but there is twist you can make one dic using multiple list

dic_list = {
    "m": pd.Series([1, 2, 3, 4]),
    "i": pd.Series([5, 6, 7, 8]),
    "t": pd.Series([9, 10, 11, 12]),
    "e": pd.Series([13, 14, 15, 16]),
}
df_1 = pd.DataFrame(dic_list)

print(df_1)
print(type(df_1))


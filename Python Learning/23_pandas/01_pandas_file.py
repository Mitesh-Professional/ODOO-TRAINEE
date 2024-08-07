import pandas as pd

list = [1,2,3,4]

var = pd.Series(list)
print("Pandas Series:-",var)

print("Type Of Pandas Series Function:-", type(var))

print("Access Value is Series:", var[2])

new_var = pd.Series(list,["a","b","c","d"])
print("Change Index Value Using Series:-")
print(new_var)

new_var = pd.Series(list,["a","b","c","d"],dtype=float)
print("Change DType Value Using Series:-")
print(new_var)

dic = {"name":["mitesh", "raj", "Hamid"],
       "age": [12,11,13]}
dic_var = pd.Series(dic)
print(dic_var)


# Single Value to make Series Using Index

index_list = pd.Series(12,index=[1,2,3,4,5,6,7,8,9])
print(index_list)


# Sum of Two Series
s1 = pd.Series([1,2,3,4,5,6,7,8])
s2 = pd.Series([11,12,13,14])

print("Sum Of a Series:- ")
print(s1+s2)
import pandas as pd

var_1 = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [6, 7, 8, 9, 10]})
var_2 = pd.DataFrame({"A": [1, 2, 3, 5, 6], "B": [11, 12, 13, 14, 15]})

# print(pd.merge(var_1, var_2, on="A"))

# left = fist var
# right = second var
# inner means unique data
# outer = all the data
# indicator =  True means it's showing which merge performed left_index=True, right_index=True
# print(pd.merge(var_1, var_2, how="outer",indicator=True))
# left_index and right_index it's showing index of left and right with data
# print(pd.merge(var_1, var_2, left_index=True, right_index=True))

# suffixes change metadata name
# print(pd.merge(var_1, var_2, left_index=True, right_index=True, suffixes=("name", "value")))

var_1 = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [6, 7, 8, 9, 10]})
var_2 = pd.DataFrame({"A": [1, 3, 5], "B": [12, 14, 16]})

sr1 = pd.Series([1, 2, 3, 4])
sr2 = pd.Series([5, 6, 7, 8])
# print(pd.concat([sr1, sr2]))
# print(pd.concat([var_1, var_2], axis=1))
# print(pd.concat([var_1, var_2], axis=1,join="inner"))
# print(pd.concat([var_1, var_2], axis=1, keys=["d1", "d2"]))

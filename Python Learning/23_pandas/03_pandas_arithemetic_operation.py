# Pandas Arithemetic Operations
import pandas as pd

dic_list = {
    "m": pd.Series([1, 2, 3, 4]),
    "i": pd.Series([5, 6, 7, 8]),
    "t": pd.Series([9, 10, 11, 12]),
    "e": pd.Series([13, 14, 15, 16]),
}
df = pd.DataFrame(dic_list)
print(df)

print("Addition")
df["s"] = df['t'] + df['e']
print(df)

print("Condition Perfome")

df["h"] = df['e'] % 2 == 0
print(df)

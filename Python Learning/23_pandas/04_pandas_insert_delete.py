import pandas as pd

# insert

df = pd.DataFrame({'A':[1,2,3,4]})

# there is three part of function
# 1. index number
# 2. column Name
# 3. Value if you want to give new value of give and you want make another copy of existing value

df.insert(1,'B',[5,6,7,8])
print(df)
df.insert(2,"C", df['A'][:3])
print(df)

# Delete Function in pandas

df.pop('C')
print(df)


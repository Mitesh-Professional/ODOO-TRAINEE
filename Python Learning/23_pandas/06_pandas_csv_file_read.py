import pandas as pd

# read_csv to red csv file in pandas
# nrows = 1 means one row
# usecols = ['a'] get you one cal also ['a', 'b'] also pass index of a cols
# skiprows = 1 means you want to skip one row in csv file
# index_col = 'b' means which columns you want make as index
# header=2 means you are make second row as a header
# names=["hello","i","am","Header"] make supper header
# header = none and use prifix = 'col1'
# dtype = {} columns convert in another data type

df = pd.read_csv('new_df.csv',dtype={"a":float})

print(df)
# print(type(df))
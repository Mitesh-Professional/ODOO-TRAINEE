# Pandas CSV File
import pandas as pd

dic_file = {"a": [1, 2, 3, 4], "b": [5, 6, 7, 8], "c": [9, 10, 11, 12], "d": [13, 14, 15, 16]}
df = pd.DataFrame(dic_file)
print(df)

# Create CSV file
#hader arg to change hader
df.to_csv("new_df.csv",index=False)
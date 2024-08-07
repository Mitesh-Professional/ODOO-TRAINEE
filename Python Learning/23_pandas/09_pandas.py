import pandas as pd
import numpy as np

# csv_01 = pd.read_csv('Shopping Mall Customer Segmentation Data .csv')
# print(csv_01.index)

# csv_01 = pd.read_csv('Shopping Mall Customer Segmentation Data .csv')
# print(csv_01.columns)

# csv_01 = pd.read_csv('Shopping Mall Customer Segmentation Data .csv')
# print(csv_01.head(10))

# csv_01 = pd.read_csv('Shopping Mall Customer Segmentation Data .csv')
# print(csv_01.index.array)

# csv_01 = pd.read_csv('Shopping Mall Customer Segmentation Data .csv')
# print(csv_01.to_numpy())

# csv_01 = pd.read_csv('Shopping Mall Customer Segmentation Data .csv')
# print(np.asarray(csv_01))

# csv_01 = pd.read_csv('Shopping Mall Customer Segmentation Data .csv')
# print(csv_01.sort_index(axis=0, ascending=False))

# csv_01 = pd.read_csv('Shopping Mall Customer Segmentation Data .csv')
# csv_01.loc[0,"Age"] = 100
# print(csv_01)

# csv_01 = pd.read_csv('Shopping Mall Customer Segmentation Data .csv')
# print(csv_01.loc[[2,4,6,8,10],["Age", "Gender", "Annual Income"]])

# csv_01 = pd.read_csv('Shopping Mall Customer Segmentation Data .csv')
# print(csv_01.iloc[0,0])

csv_01 = pd.read_csv('Shopping Mall Customer Segmentation Data .csv')

print(csv_01.drop("Annual Income", axis=1))

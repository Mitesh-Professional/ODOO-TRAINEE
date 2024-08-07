import pandas as pd

# csv_01 = pd.read_csv('Shopping Mall Customer Segmentation Data .csv',nrows=25)
# print(csv_01)

# csv_01 = pd.read_csv('Shopping Mall Customer Segmentation Data .csv',usecols=['Gender'])
# print(csv_01)

# csv_01 = pd.read_csv('Shopping Mall Customer Segmentation Data .csv',skiprows=[1,3])
# print(csv_01)

# csv_01 = pd.read_csv('Shopping Mall Customer Segmentation Data .csv', index_col="Customer ID")
# print(csv_01)

# csv_01 = pd.read_csv('Shopping Mall Customer Segmentation Data .csv', header= 4)
# print(csv_01)

# csv_01 = pd.read_csv('Shopping Mall Customer Segmentation Data .csv', names = ["col_1", "col_2", "col_3", "col_4", "col_5"])
# print(csv_01)


# csv_01 = pd.read_csv('Shopping Mall Customer Segmentation Data .csv',header=None, prefix = 'col')
# print(csv_01)

csv_01 = pd.read_csv('Shopping Mall Customer Segmentation Data .csv', dtype={"Annual Income": float})
print(csv_01)


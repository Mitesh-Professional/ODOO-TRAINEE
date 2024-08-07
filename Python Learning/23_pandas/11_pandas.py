import pandas as pd

csv = pd.read_csv('Shopping Mall Customer Segmentation Data .csv')
print(csv)

# print(csv.replace(to_replace=1, value=18))
# print(csv.replace([1, 2, 3], 18))
# print(csv.replace("[A-Za-z]", "Java", regex=True))

# This most important method in replace it replace original data in csv file
# print(csv.replace(1, method="ffill", limit=2,inplace=True))

# print(csv.interpolate())

# print(csv.interpolate(method="linear"))
# print(csv.interpolate(method="linear", limit=2))
# print(csv.interpolate(method="linear",limit_direction="backward",limit=2))
# print(csv.interpolate(method="linear",limit_area="outside"))

import pandas as pd

csv = pd.read_csv("Shopping Mall Customer Segmentation Data .csv")
# print(csv.dropna())
# print(csv)

print(csv)
print()
# print(csv.fillna({"Age": 18, "Gender": "Male","Annual Income": 600000}))
print(csv.fillna(method="backfill"))
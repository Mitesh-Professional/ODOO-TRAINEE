# Pandas Module

# 1} Pandas Series:-

## Pandas Series is give 1D array

## pandas.Series(list)

## pandas.Series(list, index_change)

## Ex. pandas.Series(list_x, index=['a', 'b', 'c'])

## pandas.Series(list,dtype = 'int')

## pandas.Series(list,name = "Data_Name")

## pandas.Series(dictionary) # accept Dictionary value

* Dtype return Object
* we make one value to Series
* we can check data type using type function
* if I have one value but i want same value multiple data so you given index it make replica of value

## Ex. pandas.Series(13,index=[1,2,3,4,5])

## pandas not give broadcast error

## Ex. pandas.Series(list=[1,2,3,4,5,6])

## Ex. pandas.Series(list=[1,2,3,4])

## print(a+b)

## this is return sum of number to index 3

## After that not give sum return NaN

## NaN means = Not a Number

# 2} Pandas DataFrame:-

## Ex. pandas.DataFrame(list)

## Ex. pandas.DataFrame(dictionary)

## when ever you pass dictionary so you can give equal amount data set

## Ex. pandas.DataFrame({"1": [1,2,3,4],"2":[1,2,3,4],"3":[5,6,7,8],"4": [1,3,5,7]})

## if you want one column you can give parameter

## Ex. pandas.DataFrame(list,column = [1])

## return 1 number Column

## Series as DataFrame also change index

## Ex. pandas.DataFrame(list,index = [1,2,3,4])

## How to particular data

## print(dataframe["Column"]["Row"])

## How to make DataFrame Using Series

## Ex. pandas.Series({"1": pandas.Series(list1),"2": pandas.Series(list2),})

## Pandas Arithmetic Operation:-

## Ex. data_frame["c"] = data_frame["1"] + data_frame["2"]

## this is Create new Column in dataframe

## All Arithmetic operation are have panda DataFrame

## Conditional Operation:-

## data_frame["New Column Name"] = data_frame[0]>=2

## return type is True And False

## Insert and Delete Data in DataFrame

## data_frame.insert(column_index,"Name of New Column",value you want give)

## data_frame.insert(1,"python",data_frame["1"])

## data_frame["New Column"] = [0,1,2,3,4]

## pop_data = data_frame.pop("Column_Name")

## del data_frame["Column_Name"]

# Pandas Csv File

## CSV = Comma Separated Value

## Create CSV File

## Ex. df = pd.DataFrame(dictionary)

## df.to_csv("CSV File Name.csv")

## How to index remove in csv file

## df.to_csv("filename.csv",index = False)

## df.to_csv("filename.csv",index = False, header = [1,2,3])

## Csv File read in python using pandas

## csv_01 = pd.read_csv('Shopping Mall Customer Segmentation Data .csv')

## print(csv_01)

## Limited Row Access Using nrows

## csv_01 = pd.read_csv('Shopping Mall Customer Segmentation Data .csv', nrows = 25)

## print(csv_01)

## Column get Using usecols

## csv_01 = pd.read_csv('Shopping Mall Customer Segmentation Data .csv', usecols = ['Gender'])

## print(csv_01)

## also use usecols=[index]

## Ex. usecols = [1]

## Skip Rows

## Ex. skiprows = [0]

## index_col = "Column Name"

## Ex. index_col = "Customer ID"

## header = index number

## Ex. header = 12

## it's change value of header

## Names = [name of col]

## names = ['col_1','col_2','col_3']

## Header = None

## Prefix = "Col"

## This method are removing in latest version

## dtype = {}

## Ex. dtype = {column name : type}

## Ex. dtype = {"Col1": float}

# Pandas Functions:-

## index

## Ex.csv_01 = pd.read_csv('Shopping Mall Customer Segmentation Data .csv')

## print(csv_01.index)

## Output = RangeIndex(start=0, stop=49, step=1)

## Describe

## Ex. csv_1.describe()

## How to get fix amount in data set

## .head()

## it's give first five value

## when give parameter in head file

## work as index and give this index to data

## .tail()

## same as head but bottom data give

## also directly use slicing

## Ex. csv_1[:2]

## csv_1.index.array

## return array of index

## How to convert csv file into numpy array

## csv_1.to_numpy()

## Second method

## numpy.asarray(csv_1)

## Sort_index

## Ex. csv_01 = pd.read_csv('Shopping Mall Customer Segmentation Data .csv')

## print(csv_01.sort_index(axis=0, ascending=False))

## it's Revers csv File

## how to change value of particular Index Value

## csv_1.loc[index number, "Column"] = "new Value"

## Ex. csv_01 = pd.read_csv('Shopping Mall Customer Segmentation Data .csv')

## csv_01.loc[0,"Age"] = 100

## print(csv_01)

## loc use for a get element in csv file

## Ex. csv_01 = pd.read_csv('Shopping Mall Customer Segmentation Data .csv')

## print(csv_01.loc[[2,4,6,8,10],["Age", "Gender", "Annual Income"]])

## if use want all the data .loc[:,[column name]]

## iloc This is use When we want Specific data

## drop this is use for drop a column

# Handling Missing Values in pandas:-

## csv.dropna() this remove NaN Value

## csv,dropna() is have axis parameter

## Ex. csv = pd.read_csv("Shopping Mall Customer Segmentation Data .csv")

## print(csv.dropna())

## csv.dropna(how = "any/all")

## any means is remove all NaN value

## all means is Remove NaN row but hole row is NaN

## csv.dropna(subset=["Column Name"])

## this is use for remove data in particular column

## csv.dropna(inplace = True)

## create new csv data and remove all the NaN Value

## csv.dropna(thresh = 1)

## means which row having one NaN Value

## csv.fillna("Value")

## fillna is use for empty NaN value change using particulaer value

## Ex. print(csv.fillna({"Age": 18, "Gender": "Male","Annual Income": 600000}))

## when ever we pass data in fillna in as dictionary so this target particular column

## csv.fillna(method = "ffill")

## this means is forward filling

## next row is NaN value filling by Currant value

## csv.fillna(method="backfill")

## same as upper and reverse filled by bottom

## axis is available

# Handle Missing values (Replace & Interpolate)

## Replace Function:-

## Ex. print(csv.replace(to_replace=1, value=18))

## Ex. print(csv.replace([1, 2, 3], 18))

## Replace using regex

## Ex. print(csv.replace("[A-Za-z]", "Java", regex=True))

## Replace in filling:-

## Ex. print(csv.replace(1, method="ffill"))

## Ex. print(csv.replace(1, method="bfill"))

## Replace with limit:-

## print(csv.replace(1, method="ffill", limit=2))

## inplace is most important method in replace it replace original data in csv file

## print(csv.replace(1, method="ffill", limit=2,inplace=True))

## Interpolate:-

## Ex. print(csv.interpolate())

## Method type = ['linear', 'time', 'index', 'values', 'nearest', 'zero', 'slinear', 'quadratic', 'cubic', 'barycentric', 'krogh', 'spline', 'polynomial', 'from_derivatives', 'piecewise_polynomial', 'pchip', 'akima', 'cubicspline']

## print(csv.interpolate(method="linear"))

## print(csv.interpolate(method="linear",limit = 2))

## print(csv.interpolate(method="linear",limit_direction="backward"))

## print(csv.interpolate(method="linear",limit_area="inside"))

## print(csv.interpolate(method="linear",limit_area="outside"))

# Merging & Concat :-

## on is merge coman part

## print(pd.merge(var_1, var_2, on="A"))

## left = fist var

## right = second var

## inner means unique data

## outer = all the data

## indicator = True means it's showing which merge performed left_index=True, right_index=True

## print(pd.merge(var_1, var_2, how="outer",indicator=True))

## left_index and right_index it's showing index of left and right with data

## print(pd.merge(var_1, var_2, left_index=True, right_index=True))

## suffixes change metadata name

## print(pd.merge(var_1, var_2, left_index=True, right_index=True, suffixes=("name", "value")))

## Concat :-

## print(pd.concat([sr1, sr2]))

## print(pd.concat([var_1, var_2], axis=1))

## print(pd.concat([var_1, var_2], axis=1,join="inner"))

## print(pd.concat([var_1, var_2], axis=1, keys=["d1", "d2"]))

#
# Wiki

## 1 Which Package/Library did I select?
I chose the Pandas package for Python. 
## 2 What is the package/library?
### What purpose does it serve?
Pandas is a data analysis Package and it is used to parse, manipulate and analyze data using python. It is used in many different fields to do data analysis and is a very popular option for analysists. 
### How do you use it?
Pandas can do many things revolving around data and data manipulation using an object that is in the package called a **DataFrame**. DataFrames have intgrated indexing to help with data management. Pandas has many different tools for reading and writing data from different files such as; csv files, text files, Excel spreadsheets, SQL databases and the HDF5 format [ref](https://pandas.pydata.org/about/). Like SQL you can manipulate the dataframes to parse specific data in the dataframes, using things like conditional statements and various built-in methods can narrow in on specific data points. Also, Pandas has merging and joining systems so you can handle a lot of dataframes at once and search through all of them using a key. Pandas works a lot like SQL in that you can have many dataframes that you can interact with and search through, however there are no relationships like in an actual database so each dataframe is an individual object that is not reliant on anything else. It can be used in many settings where you record and manage data, and it is very conveinient because Python is a very popular language so many people can use it and benefit from its many capabilities. 

## 3 What are the functionalities of the package?
Pandas can take arrays and turn them into tables [ref](https://www.w3schools.com/python/pandas/pandas_dataframes.asp): 
```
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df)
```
Output: 
|     |calories|duration|
|-----------------------|
|  0  |420|           50|
|  1  |380|           40|
|  2  |390|           45|

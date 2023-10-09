# Wiki

## 1 Which Package/Library did I select?
I chose the Pandas package for Python. 
## 2 What is the package/library?
Pandas is a data analysis Package and it is used to parse, manipulate and analyze data using python.
### What purpose does it serve?
It is used in many different fields to do data analysis and is a very popular option for analysists. 
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
|index|calories|duration|
|-----|-----|-----------|
|  0  | 420 | 50 |
|  1  | 380 | 40 |
|  2  | 390 | 45 |

## 4 When was it created?
Pandas was started in 2008 and in 2009 it became open source.
## 5 Why did I choose this package?
I chose this package because I would like to try data analysis in the future and would like to have a head start on learning about it and the data analysis field. The reason i chose Pandas specifically is because i saw it was very popular among data analysts and one of my friends had reccommended that I use Pandas if I were to do anything data science related. 
## 6 How did learning the package influence the learning of the language? 
I think that learning this package helped me get familliar with using python and file I/O, it has also helped with any kind of data management using python as i now know how to use data in python. It also helps to learn new things in python because it will help me learn other new languages/packages faster because i now have more expirience with learning new things.
## 7 How was the overall expirience with the package? 

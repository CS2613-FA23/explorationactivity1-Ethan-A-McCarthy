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

Pandas can select data by the label of each column [ref](https://pandas.pydata.org/docs/user_guide/10min.html):
```
In [27]: df.loc[dates[0]]
Out[27]: 
A    0.469112
B   -0.282863
C   -1.509059
D   -1.135632
Name: 2013-01-01 00:00:00, dtype: float64
```
Pandas can calculate the mean of columns and rows [ref](https://pandas.pydata.org/docs/user_guide/10min.html):
```
In [61]: df.mean()
Out[61]: 
A   -0.004474
B   -0.383981
C   -0.687758
D    5.000000
F    3.000000
dtype: float64
```
Pandas can join together DataFrames kind of like how the SQL join method [ref](https://pandas.pydata.org/docs/user_guide/10min.html):
```
In [77]: left = pd.DataFrame({"key": ["foo", "foo"], "lval": [1, 2]})

In [78]: right = pd.DataFrame({"key": ["foo", "foo"], "rval": [4, 5]})

In [79]: left
Out[79]: 
   key  lval
0  foo     1
1  foo     2

In [80]: right
Out[80]: 
   key  rval
0  foo     4
1  foo     5

In [81]: pd.merge(left, right, on="key")
Out[81]: 
   key  lval  rval
0  foo     1     4
1  foo     1     5
2  foo     2     4
3  foo     2     5
```
Pandas can also localize to time zones and also convert to different time zones [ref](https://pandas.pydata.org/docs/user_guide/10min.html)
```
In [107]: rng = pd.date_range("3/6/2012 00:00", periods=5, freq="D")

In [108]: ts = pd.Series(np.random.randn(len(rng)), rng)

In [109]: ts
Out[109]: 
2012-03-06    1.857704
2012-03-07   -1.193545
2012-03-08    0.677510
2012-03-09   -0.153931
2012-03-10    0.520091
Freq: D, dtype: float64

In [110]: ts_utc = ts.tz_localize("UTC")

In [111]: ts_utc
Out[111]: 
2012-03-06 00:00:00+00:00    1.857704
2012-03-07 00:00:00+00:00   -1.193545
2012-03-08 00:00:00+00:00    0.677510
2012-03-09 00:00:00+00:00   -0.153931
2012-03-10 00:00:00+00:00    0.520091
Freq: D, dtype: float64
```
As you can see Pandas has many features that can be used in everyday work and in many different fields.

## 4 When was it created?
Pandas was started in 2008 and in 2009 it became open source.
## 5 Why did I choose this package?
I chose this package because I would like to try data analysis in the future and would like to have a head start on learning about it and the data analysis field. The reason i chose Pandas specifically is because i saw it was very popular among data analysts and one of my friends had reccommended that I use Pandas if I were to do anything data science related. 
## 6 How did learning the package influence the learning of the language? 
I think that learning this package helped me get familliar with using python and file I/O, it has also helped with any kind of data management using python as i now know how to use data in python. It also helps to learn new things in python because it will help me learn other new languages/packages faster because i now have more expirience with learning new things.
## 7 How was the overall expirience with the package? 
The package was pretty straightforward and easy to learn and use. It helps that i have taken a course in databases and already had a little expirience handling data like this.
### When would you reccommend this package to others? 
I would reccommend this package to anyone who is into data analytics or any data related things. I would also reccommend this to anyone who might want to learn data analysis because this is very beginner friendly and can be used by anyone.
### Would you continue using this package?
Yes. I found it very easy to use and it was fairly easy to learn and apply what i learned when doing this project. It was definitly very accessible and was an interesting to play around with and if i ever need to track data for any reason i would very much be inclined to use Pandas.

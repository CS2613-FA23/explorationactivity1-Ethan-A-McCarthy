#Ethan McCarthy
#Exploration Activity 1 

import pandas

#read in file 
#in this example i have the global salary data and it is automatically sorted alphabetically 
dataframe = pandas.read_csv('salary_data.csv')

#output the data
print("Sorted by name of country:")
print(dataframe)

#parsing data using conditions 
dataframe_condition = dataframe.loc[dataframe.median_salary > 4000]
print("Countries where the median salary is over 4000$: ")
print(dataframe_condition)

#compute average salary of each continent
cont_average_salary = dataframe.groupby('continent_name')['average_salary'].mean()
print("Average salary of each continent:")
print(cont_average_salary)

#find the top 5 countries with the highest salary
highest_salary = dataframe.sort_values(by= ['highest_salary'], ascending=False)
print("Top 5 countries with the highest salaries:")
print(highest_salary.head(5))

#we can combine the previous querys to get the top 3 highest salaries in each continent
print("Top 3 highest salaries in each continent:")
na_highest = highest_salary.groupby(['continent_name'])
na_highest = na_highest.get_group("Northern America")
print(na_highest.head(3))

eu_highest = highest_salary.groupby(['continent_name'])
eu_highest = eu_highest.get_group("Europe")
print(eu_highest.head(3))

africa_highest = highest_salary.groupby(['continent_name'])
africa_highest = africa_highest.get_group("Africa")
print(africa_highest.head(3))

asia_highest = highest_salary.groupby(['continent_name'])
asia_highest = asia_highest.get_group("Asia")
print(asia_highest.head(3))

carr_highest = highest_salary.groupby(['continent_name'])
carr_highest = carr_highest.get_group("Caribbean")
print(carr_highest.head(3))

central_highest = highest_salary.groupby(['continent_name'])
central_highest = central_highest.get_group("Central America")
print(central_highest.head(3))

north_highest = highest_salary.groupby(['continent_name'])
north_highest = north_highest.get_group("North America")
print(north_highest.head(3))

oc_highest = highest_salary.groupby(['continent_name'])
oc_highest = oc_highest.get_group("Oceania")
print(oc_highest.head(3))

sa_highest = highest_salary.groupby(['continent_name'])
sa_highest = sa_highest.get_group("South America")
print(sa_highest.head(3))
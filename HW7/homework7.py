# PPHA 30535
# Spring 2022
# Homework 7

# Sai Omkar Kandukuri

# Sai Omkar Kandukuri
# S-Omkar-K

# Due date: Sunday May 22nd before midnight
# Write your answers in the space between the questions, and commit/push only
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put
# thought into your work.

##################

# Question 1: Explore the data portals for the OECD and the World Bank.  Pick
# any three countries, and pick two data series from each of the OECD and the
# World Bank that covers these places over some time period.  It's ok if
# frequency doesn't match up (e.g. one is monthly and one is quarterly), but
# you will need to handle the aggregation.  Load the data into dataframes using
# Pandas data_reader, then merge the data together in long (tidy) format, and
# write it to a csv document that you commit to your repo.


import pandas as pd
import datetime
import pandas_datareader.data as web
from pandas_datareader import wb
from pandas_datareader import oecd
import requests



#indicator = 'NY.GDP.MKTP.CD'
#country = ['US','IN','FR']
#start = datetime.date(year=2000, month=1,  day=1)
#end   = datetime.date(year=2010, month=12, day=31)
#wb_data = wb.download(indicator=indicator, 
 #                country=country, 
#                 start=start, end=end)







##Method 1
indicator = ['NY.GDP.MKTP.CD','EG.ELC.ACCS.ZS']
country = ['US','AU','FR']
start = datetime.date(year=2000, month=1,  day=1)
end   = datetime.date(year=2010, month=12, day=31)
wb_data = wb.download(indicator=indicator, country=country, start=start, end=end)

wb_data.head()
wb_data.reset_index(inplace = True)
wb_data = wb_data.rename(columns = {'NY.GDP.MKTP.CD': 'GDP','EG.ELC.ACCS.ZS':'Perct. Access to Electricity'})
wb_data['country'] = wb_data['country'].astype(str)
wb_data['year'] = wb_data['year'].astype(str)

#OECD data
oecd_data = web.DataReader('HISTPOP', 'oecd', 2000, 2010)
oecd_debt_data = web.DataReader('GOV_DEBT', 'oecd', 2000, 2010)
#Country United States
oecd_data_US = oecd_data["United States"]["Total"]["Total"]
oecd_data_US
oecd_data_US = oecd_data_US.to_frame()
oecd_data_US["country"] = 'United States'
oecd_data_US.reset_index(inplace = True)
#Country France
oecd_data_FR = oecd_data["France"]["Total"]["Total"]
oecd_data_FR
oecd_data_FR = oecd_data_FR.to_frame()
oecd_data_FR["country"] = 'France'
oecd_data_FR.reset_index(inplace = True)
#Country Australia
oecd_data_AU = oecd_data["Australia"]["Total"]["Total"]
oecd_data_AU
oecd_data_AU = oecd_data_AU.to_frame()
oecd_data_AU["country"] = 'Australia'
oecd_data_AU.reset_index(inplace = True)
#Concatenate country data and make it usable
oecd_all = pd.concat([oecd_data_US, oecd_data_AU, oecd_data_FR], axis = 0)
oecd_all['Time'] = oecd_all['Time'].dt.year
oecd_all = oecd_all.rename(columns = {'Time':'year', 'Total':'Population'})
oecd_all['year'] = oecd_all['year'].astype(str)
oecd_all['country'] = oecd_all['country'].astype(str)

data_final = wb_data.merge(oecd_all, on = ['country','year'], how = 'inner')

#OECD debt data for Country France
oecd_debt_data_FR = oecd_debt_data["France"]['Stocks: Outstanding amounts']['Annual']['Million USD']['Total central government debt']
oecd_debt_data_FR = oecd_debt_data_FR.to_frame()
oecd_debt_data_FR.reset_index(inplace = True)
oecd_debt_data_FR['country'] = 'France'
oecd_debt_data_FR.index

#OECD debt data for Country United States
oecd_debt_data_US = oecd_debt_data["United States"]['Stocks: Outstanding amounts']['Annual']['Million USD']['Total central government debt']
oecd_debt_data_US = oecd_debt_data_US.to_frame()
oecd_debt_data_US.reset_index(inplace = True)
oecd_debt_data_US['country'] = 'United States'
oecd_debt_data_US.index

#OECD debt data for Country Australia
oecd_debt_data_AU = oecd_debt_data["Australia"]['Stocks: Outstanding amounts']['Annual']['Million USD']['Total central government debt']
oecd_debt_data_AU = oecd_debt_data_AU.to_frame()
oecd_debt_data_AU.reset_index(inplace = True)
oecd_debt_data_AU['country'] = 'Australia'
oecd_debt_data_AU.index

#Concatenate all three country data
oecd_debt_all = pd.concat([oecd_debt_data_US, oecd_debt_data_AU, oecd_debt_data_FR], axis = 0)

#Renaming the columns and changing types to make it usable
oecd_debt_all['Time period'] = oecd_debt_all['Time period'].dt.year
oecd_debt_all = oecd_debt_all.rename(columns = {'Time period': 'year'})
oecd_debt_all['year'] = oecd_debt_all['year'].astype(str)
data_final = data_final.merge(oecd_debt_all, on = ['country','year'], how = 'inner')


#Modifying it to the desiredlong format
columns_2 = ['GDP', 'Perct. Access to Electricity', 'Population', 'Total central government debt']
columns_1 = ['country', 'year']
data_final = pd.melt(data_final, id_vars = columns_1, value_vars = columns_2, var_name = 'Indicators', value_name = 'Values')

#Providing the 4 different ways of long forms as the format was not specified

#Option 0 : Direct melt to get a long form 
data_final = pd.melt(data_final, id_vars = columns_1, value_vars = columns_2)
data_final.to_csv('C:/Users/saiom/OneDrive/Documents/GitHub/homework-7-S-Omkar-K/data_final_Option0.csv')


#Option 1: Another long format for the data, by setting index that gives another form
#data_final.set_index(['country','Year'], inplace = True)
#data_final.to_csv('C:/Users/saiom/OneDrive/Documents/GitHub/homework-7-S-Omkar-K/data_final_Option1.csv')


#Option 2: Can use the stack function to make the long form it more informative form
#data_final = pd.melt(data_final, id_vars = columns_1, value_vars = columns_2)
#data_final.stack()

#Option 3: We can transform the order by sorting according to year and then applying melt to extract a different form
#data_final2 = pd.melt(data_final2, id_vars = columns_1, value_vars = columns_2)
#data_final = pd.melt(data_final2, id_vars = columns_1, value_vars = columns_2)
#data_final = data_final.sort_values(by=['country', 'Year'])
#data_final.to_csv('C:/Users/saiom/OneDrive/Documents/GitHub/homework-7-S-Omkar-K/data_final_option3.csv')


#Option 4: Combining Index to make a meaningful form 
#data_final = pd.melt(data_final, id_vars = columns_1, value_vars = columns_2, var_name = 'Indicators', value_name = 'Values')
#data_final = data_final.sort_values(by=['country', 'Year'])
#data_final.set_index(['country','Year'], inplace = True)
#data_final.to_csv('C:/Users/saiom/OneDrive/Documents/GitHub/homework-7-S-Omkar-K/data_final_option4.csv')





#-----------------------------------------------------------------------------#




###Method 2, Using dynamic variables and for loop to construct/clean data, increase efficiency of code
#World bank data , 2 indicators, GDP and Electricity access, Annual frequency
indicator = ['NY.GDP.MKTP.CD','EG.ELC.ACCS.ZS']
country = ['US','AU','FR']
start = datetime.date(year=2000, month=1,  day=1)
end   = datetime.date(year=2010, month=12, day=31)
wb_data2 = wb.download(indicator=indicator, country=country, start=start, end=end)
wb_data2.head()
wb_data2.reset_index(inplace = True)
wb_data2 = wb_data2.rename(columns = {'NY.GDP.MKTP.CD': 'GDP','EG.ELC.ACCS.ZS':'Perct. Access to Electricity', 'year':'Year'})
wb_data2.dtypes
wb_data2['country'] = wb_data2['country'].astype(str)
wb_data2['Year'] = wb_data2['Year'].astype(str)


##OECD data, 2 indicators, Government debt and historical population, Annual frequency
oecd_debt_data = web.DataReader('GOV_DEBT', 'oecd', 2000, 2010)
oecd_pop_data = web.DataReader('HISTPOP', 'oecd', 2000, 2010)

country_dict= {'FR': "France", 'US': 'United States', 'AU':'Australia'}
oecd_debt_data2_FR = []
oecd_debt_data2_US = []
oecd_debt_data2_AU = []
oecd_pop_data2_FR = []
oecd_pop_data2_US = []
oecd_pop_data2_AU = []

#Using dynamic variables to create datasets for each each country, indicator
for key in country_dict.keys():
    variable = f"oecd_debt_data2_{key}"
    variable2 = f"oecd_pop_data2_{key}"
    
    #For debt data
    vars()[variable] = oecd_debt_data[country_dict[key]]['Stocks: Outstanding amounts']['Annual']['Million USD']['Total central government debt']
    vars()[variable] = vars()[variable].to_frame()
    vars()[variable].reset_index(inplace = True)
    vars()[variable].insert(2, 'country',country_dict[key])
    vars()[variable] = vars()[variable].rename(columns = {"Time period": "Year", "Total central government debt": "Debt"})
    
    
    #For population data
    vars()[variable2] = oecd_pop_data[country_dict[key]]["Total"]["Total"]
    vars()[variable2] = vars()[variable2].to_frame()
    vars()[variable2].reset_index(inplace = True)
    vars()[variable2].insert(2, 'country',country_dict[key])
    vars()[variable2] = vars()[variable2].rename(columns = {"Time": "Year", "Total": "Population"})


oecd_debt2_all = pd.concat([oecd_debt_data2_US, oecd_debt_data2_AU, oecd_debt_data2_FR], axis = 0)
oecd_debt2_all['Year'] = oecd_debt2_all['Year'].dt.year
oecd_pop2_all = pd.concat([oecd_pop_data2_US, oecd_pop_data2_AU, oecd_pop_data2_FR], axis = 0)
oecd_pop2_all['Year'] = oecd_pop2_all['Year'].dt.year
#merge OECD population data and debt data
oecd_final = oecd_debt2_all.merge(oecd_pop2_all, on = ['country', 'Year'], how = 'inner')
oecd_final['country'] = oecd_final['country'].astype(str)
oecd_final['Year'] = oecd_final['Year'].astype(str)
#Merging wb data and oecd data for our final data
data_final2 = wb_data2.merge(oecd_final, on = ['country','Year'], how = 'inner')
data_final2['country'] = data_final2['country'].astype(str)
data_final2['Year'] = data_final2['Year'].astype(str)
#long format
columns_2 = ['GDP', 'Perct. Access to Electricity', 'Debt', 'Population']
columns_1 = ['country', 'Year']
#data_final2 = pd.melt(data_final2, id_vars = columns_1, value_vars = columns_2)
#data_final2.to_csv('C:/Users/saiom/OneDrive/Documents/GitHub/homework-7-S-Omkar-K/data_final2.csv')




#Providing the 4 different ways of long forms as the format was not specified
#Option 0 : Direct melt to get a long form 
data_final2 = pd.melt(data_final2, id_vars = columns_1, value_vars = columns_2)
data_final2.to_csv('C:/Users/saiom/OneDrive/Documents/GitHub/homework-7-S-Omkar-K/data_final2_Option0.csv')


#Option 1: Another long format for the data, by setting index that gives another form
data_final2.set_index(['country','Year'], inplace = True)
data_final2.to_csv('C:/Users/saiom/OneDrive/Documents/GitHub/homework-7-S-Omkar-K/data_final2_Option1.csv')


#Option 2: Can use the stack function to make another long form form
data_final2 = pd.melt(data_final2, id_vars = columns_1, value_vars = columns_2, var_name = 'Indicators', value_name = 'Values')
data_final2.stack()
data_final2.to_csv('C:/Users/saiom/OneDrive/Documents/GitHub/homework-7-S-Omkar-K/data_final2_Option2.csv')


#Option 3: We can transform the order by sorting according to year and then applying melt to extract a different form
#data_final2 = pd.melt(data_final2, id_vars = columns_1, value_vars = columns_2)
data_final2 = pd.melt(data_final2, id_vars = columns_1, value_vars = columns_2, var_name = 'Indicators', value_name = 'Values')
data_final2 = data_final2.sort_values(by=['country', 'Year'])
data_final2.to_csv('C:/Users/saiom/OneDrive/Documents/GitHub/homework-7-S-Omkar-K/data_final2_option3.csv')


#Option 4: Combining Index to make a meaningful form 
data_final2 = pd.melt(data_final2, id_vars = columns_1, value_vars = columns_2, var_name = 'Indicators', value_name = 'Values')
data_final2 = data_final2.sort_values(by=['country', 'Year'])
data_final2.set_index(['country','Year'], inplace = True)
data_final2.to_csv('C:/Users/saiom/OneDrive/Documents/GitHub/homework-7-S-Omkar-K/data_final2_option4.csv')

#-----------------------------------------------------------------------------#


# Question 2: On the following Harris School website:
# https://harris.uchicago.edu/academics/programs-degrees/degrees/master-public-policy-mpp
# There is a list named Curriculumn after Program Details, explaining the core classes.
# There are 21 bullet points for this, beginning with "Analytical Politics I" and ending
# just before "Elective Options". Some of those bullet points are intented under others. 
# Using requests and BeautifulSoup, collect the text of each of these bullet points so 
# that the top level bullet points, e.g. "Analytical Politics I" are the keys in a 
# dictionary, while the bullet points representing specific classes under them are values
# in a list. The result will be a dictionary where you can index by a requirement and get
# back a list of core class options.



import requests
from bs4 import BeautifulSoup

#Method 1 using lxml, no manual matching, automated retrieval
url = 'https://harris.uchicago.edu/academics/programs-degrees/degrees/master-public-policy-mpp'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

my_dict = {}

attempt = 0
for lists in soup.find_all('li'):
    is_considerable = False
    for val in lists.find_all('p'):
        if val.get_text().startswith("6 core"):
            is_considerable = True
            attempt += 1
            break

    if is_considerable and attempt == 2:
        for ul in lists.find('ul'):
            for li in lists.find_all('li'):
                index = 0
                key = ''
                for data in li.find_all('p'):
                    result = data.get_text().strip()
                    if index == 0:
                        temp = result
                        key = temp[:len(temp)-1]
                        my_dict[key] = []
                    else:
                        my_dict[key].append(result.replace(u'\xa0', u' '))
                    index += 1

keys_to_delete = []
for key in my_dict.keys():
    if not my_dict[key]:
        keys_to_delete.append(key)

for key in keys_to_delete:
    del my_dict[key]

print(my_dict)

my_dict['Analytical Politics I']
my_dict['Microeconomics Sequence I']

#--------------------------------------------------------------------------------#


##Method 2 using html.parser
#A more efficient way, applicable to all universal websites, no manual matching, automated retrieval.
url = 'https://harris.uchicago.edu/academics/programs-degrees/degrees/master-public-policy-mpp'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
my_dict = {}

for unordered_lists in soup.find_all('ul'):
    for lists in unordered_lists.find_all('li'):
        
        is_considerable = False
        for val in lists.find_all('p'):
            if val.get_text().startswith("6 core"):
                is_considerable = True
                break

        if is_considerable:
          
            for li in lists.find_all('li'):
                index = 0
                key = ''
                for data in li.find_all('p'):
                    if index == 0:
                       key = data.get_text()
                       my_dict[key] = []
                    else:
                       my_dict[key].append(data.get_text())
                    index += 1

keys_to_delete = []
for key in my_dict.keys():
    if not my_dict[key]:
        keys_to_delete.append(key)


for key in keys_to_delete:
    del my_dict[key]

print(my_dict)


my_dict['Analytical Politics I:']
#did not clean ':' and 'or' as it was not mentioned. However, cleaned the in the method 1
my_dict['Microeconomics Sequence I']
#did not clean ':' and 'or' as it was not mentioned. However, cleaned in the method 1








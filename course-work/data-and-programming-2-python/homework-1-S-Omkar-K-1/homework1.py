# Data Skills 2
# Autumn 2022
#
# Homework 1
#
# Due Monday October 10th before midnight on Gradescope.  Please read the academic integrity
# section of the syllabus for guidelines on how to collaborate and cite sources, and the grading
# rubric posted on Canvas (under syllabus).
#
# Be sure to clean up your code, removing unnecessary elements like intermediate output that were
# only used in debugging.  Write this as if it were something you were doing for your work as a
# research assistant.  You will be graded on how well you generalize and organize your code.
#
# #################################################


import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

base_path = r'C:\Users\saiom\OneDrive\Documents\GitHub\homework-1-S-Omkar-K-1'


# 1. The two datasets included in the assignment repo are downloaded directly from the BEA.  The file
# labeled "total" has the total employment per state for the years 2000 and 2017.  The file labeled
# "by industry" has employment per industry in each of 10 industries per state for the same years.
#
# Load and merge the data into a panel dataframe, with the columns: "state", "year", and one for each
# of the 10 industries.  Every state-year combination should uniquely identify a row.  No more and no
# less than 12 columns should remain.  Do any necessary cleaning for the data to be easily usable.
#
# The values should be given as the share of the total employment in that place and time, e.g. if
# total employment in a place and time was 100, and the employment in one industry was 10, then the
# value shown for that state-year industry should be 0.1.
#
# Output this dataframe to a csv document named "data.csv" and sync it to your homework repo with
# your code.

cols = ['2000', '2017']

cols2 = ['Employed total',
       'Arts, entertainment, and recreation', 'Educational services',
       'Farm employment', 'Finance and insurance',
       'Government and government enterprises',
       'Health care and social assistance', 'Information', 'Manufacturing',
       'Mining, quarrying, and oil and gas extraction', 'Retail trade']

industries  = ['Arts, entertainment, and recreation', 'Educational services',
       'Farm employment', 'Finance and insurance',
       'Government and government enterprises',
       'Health care and social assistance', 'Information', 'Manufacturing',
       'Mining, quarrying, and oil and gas extraction', 'Retail trade']

def rename (data, old , new):
    data.rename(columns = {old:new}, inplace = True)
    return data    

"""
def data_path(path, file_name):
    data_path = os.path.join(path,file_name)
    return data_path
"""

"""
def load_csv_file (file_location, rows_toskip):
    data = pd.read_csv(file_location, skiprows = rows_toskip)
    return data
"""

"""
def drop_columns (data, columns_list):
    data = data.drop(column_list, axis = 1)
    return data
"""



#Working with total data
total_data_path = os.path.join(base_path, 'SAEMP25N total.csv')
total_data = pd.read_csv(total_data_path, skiprows = 4) #, skipfooter = 3,quoting = 3)
total_data = total_data.head(-3) ##skipfooter =3 with quoting=3 can also be used to remove footer
total_data = rename(total_data, 'GeoName', 'State' )
total_data = total_data.drop(["GeoFips"], axis = 1)
total_data[cols] = total_data[cols].apply(pd.to_numeric, errors = 'coerce')
#Reshaping Total data
total_data = pd.melt(total_data, id_vars= ['State'], 
                     value_vars= ['2000','2017'], var_name = 'Year', value_name = 'Employed total')



#Working with Industry data
industry_data_path = os.path.join(base_path, 'SAEMP25N by industry.csv')
industry_data = pd.read_csv(industry_data_path, skiprows = 4)
industry_data = industry_data.head(-5) 
industry_data = rename(industry_data, 'GeoName', 'State' )
industry_data = industry_data.drop(['GeoFips', 'LineCode'], axis = 1)
industry_data['Description'] = industry_data['Description'].str.strip()
industry_data = industry_data[industry_data['Description'] != 'By industry']
industry_data = industry_data.replace(['(T)', '(D)'], np.nan)
industry_data[cols] = industry_data[cols].apply(pd.to_numeric, errors = 'coerce')
#Reshaping Industry data
industry_data = pd.melt(industry_data, id_vars= ['State','Description'], 
                        value_vars= ['2000','2017'], var_name = 'Year', value_name = 'Employed No')
industry_data = pd.pivot(industry_data, index = ['State','Year'], columns='Description', values = 'Employed No')



#Merging Industry and Total data
merged_data = pd.merge(total_data, industry_data, on = ['State', 'Year'])
merged_data[cols2] = merged_data[cols2].apply(lambda x: x.div(merged_data['Employed total'], axis = 0))
merged_data = merged_data.drop('Employed total', axis = 1)
merged_data = merged_data.sort_values(['State','Year'])


#Export merged data to a csv file
merged_data.to_csv(os.path.join(base_path, 'merged_final_data.csv'), index= False)







# 2. Using the dataset you created, answer the following questions:
#
# a. Find the states with the top five share of manufacturing employment in the year 2000, then show
# how their share of employment in manufacturing changed between 2000 and 2017.  Use a basic plot to
# display the information.
#
# b. Show which five states have the highest concentration of employment in any single industry in each
# of 2000 and 2017, and what those industries are.





#a

merged_data_2000 = merged_data[merged_data['Year'] == '2000']
merged_data_2017 = merged_data[merged_data['Year'] == '2017']
     
def top_5 (year, industry):

     if year == 2000:
        top5 = merged_data_2000[['State',industry]].sort_values([industry], ascending = False).head() 

     if year == 2017:
        top5 = merged_data_2000[['State',industry]].sort_values([industry], ascending = False).head()

     if year not in (2000, 2017):
        print("Wrong year provided")
         
     return top5

Manuf_top5_2000 = top_5(2000, 'Manufacturing')
print(Manuf_top5_2000) 


#States with top five share of manufacturing employment in the year 2000
top_states = Manuf_top5_2000['State'].values.tolist()
Manuf_top5_2000_in_2017 = merged_data_2017[merged_data_2017.State.isin(top_states)]
Manuf_top5_2000_in_2017 = Manuf_top5_2000_in_2017[['State', 'Manufacturing']]

#Show change from 2000 to 2017
merged_top5 = pd.merge(Manuf_top5_2000, Manuf_top5_2000_in_2017, on = ['State'], suffixes = ('_2000', '_2017'))
merged_top5.plot(x = 'State', y = ['Manufacturing_2000', 'Manufacturing_2017'], 
                 kind = 'bar', 
                 title = "Change in employment in top manufacturing companies from 2000 to 2017",
                 ylabel = 'Employment share in Total employment')


#b

#Method by melt and pivot
merged_data_unmelt = pd.melt(merged_data, id_vars = ['State', 'Year'], value_vars = industries, value_name = 'Employment share', var_name = 'Industry name')
merged_data_unmelt_pivot = pd.pivot(merged_data_unmelt, index = ['State','Industry name'], columns = 'Year', values = 'Employment share')


def top5_combinations (year):
    if year in ('2000', '2017'):
        merged_unmelt = merged_data_unmelt_pivot.sort_values(year, ascending = False).head()
        print(merged_unmelt[year])
  
    if year not in ('2000','2017'):
        print('Wrong year provided')
        return

top5_combinations('2000')

top5_combinations('2017')


""" Another method without using a function
merged_unmelt_2000 = merged_data_unmelt_pivot.sort_values('2000', ascending = False).head()
print(merged_unmelt_2000['2000'])

merged_unmelt_2017 = merged_data_unmelt_pivot.sort_values('2017', ascending = False).head()
print(merged_unmelt_2017['2017'])
"""



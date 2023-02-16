# PPHA 30535
# Spring 2022
# Homework 4 and 5

# Sai Omkar Kandukuri

# Sai Omkar Kandukuri
# S-Omkar-K

# Due date: Sunday May 8th before midnight
# Write your answers in the space between the questions, and commit/push only
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put
# thought into your work. Using functions for organization will be rewarded.

# Grader: Valeria Balza
# [-2pts] Q2: Style deduction for hardcoding string conversion.
    # More robust approach is to use a method like zfill to pad strings.
# [-5pts] Q4: The long dataframe should have the columns state, year, and popestimate.
    # Your current approach is more general such that it also includes rows for state name. 
# Grade: 92/100pts

##################

# To answer these questions, you will use the two csv documents included in
# your repo.  In nst-est2019-alldata.csv: SUMLEV is the level of aggregation,
# where 10 is the whole US, 20 is a US region, and 40 is a US state. REGION
# is the fips code for the US region. STATE is the fips code for the US state
# The other values are as per the data dictionary at:
# https://www2.census.gov/programs-surveys/popest/technical-documentation/file-layouts/2010-2019/nst-est2019-alldata.pdf
# Note that each question will build on the modified dataframe from the
# question before.


import pandas as pd
# Question 1: Load the population estimates file into a dataframe. Specify
# an absolute path using the Python os library to join filenames, so that
# anyone who clones your homework repo only needs to update one for all
# loading to work.  Then show code doing some basic exploration of the
# dataframe; imagine you are an intern and are handed a dataset that your
# boss isn't familiar with, and asks you to summarize for them.



import us
import os


base_path = r'C:\Users\saiom\OneDrive\Documents\GitHub\homework-4-and-5-S-Omkar-K'
path = os.path.join(base_path, 'nst-est2019-alldata.csv')

print(path)

pop_data = pd.read_csv(path)

pop_data.shape
#We have 57 rows and 139 columns in this data frame

pop_data.columns
#We have columns such as REGION, STATE, CENSUSPOP, ESTIMATESBASE, POPESTIMATE, 
#RDOMESTICMIC, RNETMIG, some with data ranging from 2010 till 2019
pop_data.head(10)

pop_data.tail(10)

pop_data.info() #139 Columns, 57 rows

pop_data.dtypes #We have int type (84 columns) and float type (54 columns) of values

len(pop_data[pop_data['SUMLEV'] == 20])
#We have data from 4 regions in this data set

len(pop_data[pop_data['SUMLEV'] == 40])
#We have data from 52 states in this data set

len(pop_data['STATE'].unique())
#We have 53 unique values in 'STATE' column

pop_data['CENSUS2010POP'].mean()
#We have a mean of 16315129.8771 for the CENSUS2010POP column

pop_data['POPESTIMATE2019'].mean()
#Mean of population estimate is 17331794.0877193 in 2019

pop_data['RNETMIG2019'].mean()
#Mean of RNETMIG in 2019 is 1.83



# Question 2: Your data only includes fips codes for states.  Use the us
# library to crosswalk fips codes to state abbreviations.  Keep only the
# state abbreviations in your data.


pop_data['STATE'].unique()

fips_to_abbr = us.states.mapping("fips","abbr",states=None)
fips_to_abbr

pop_data['STATE'].dtype
pop_data['STATE'] = pop_data['STATE'].astype(str)
pop_data['STATE']

pop_data.loc[5:11, 'STATE'] = '0' + pop_data.loc[5:11, 'STATE'] 
pop_data['STATE']

pop_data['STATE'] = pop_data['STATE'].map(fips_to_abbr)
pop_data['STATE']

























# Question 3: Subset the data so that only observations for individual
# US states remain, and only state names and data for the population
# estimates in 2010-2019 remain.

pop_data.columns
#Adding name column as its mentioned in question
pop_data = pop_data[pop_data['SUMLEV'] == 40] 
abbr_to_names = us.states.mapping("abbr","name")
abbr_to_names

pop_data['STATE_NAME'] = pop_data['STATE'].map(abbr_to_names)
popest_column = ['STATE', 'STATE_NAME' ,'POPESTIMATE2010', 'POPESTIMATE2011', 
                 'POPESTIMATE2012', 'POPESTIMATE2013', 'POPESTIMATE2014',
                 'POPESTIMATE2015', 'POPESTIMATE2016',
                 'POPESTIMATE2017', 'POPESTIMATE2018',
                 'POPESTIMATE2019']
pop_data = pop_data[popest_column]
pop_data














# Question 4: Reshape the data from wide to long, making sure you reset
# the index to the default values if any of your data is located in the index.

pop_data

pop_data = pop_data.reset_index()

pop_data

pop_data = pd.melt(pop_data, id_vars='STATE', value_vars=popest_column)

pop_data
pop_data.head()
pop_data.tail()

pop_data_q3 = pop_data

# Question 5: Open the state-visits.csv file, and fill in the VISITED column
# with a dummy variable for whether you've visited a state or not.  If you
# haven't been to many states, then filling in a random selection of them
# is fine too.  Save your changes.  Then load the file as a dataframe in
# Python, and merge the visited column into your population dataframe, only
# keeping values that appear in both dataframes.  Are any observations
# dropped from this?  Show code where you investigate your merge, and
# display any observations that weren't in both dataframes.


pop_data_bkp = pop_data



state_visits_path = os.path.join(base_path, 'state-visits.csv')
state_visits = pd.read_csv(state_visits_path)
state_visits.head()
pop_data = pop_data.merge(state_visits, on = 'STATE', how = 'inner')
pop_data


#Investigation
pop_data.info()
#We see there are more rows in population data frame than in the merged data frame
#That means some rows are dropped in the merge
outer_merge = pop_data_bkp.merge(state_visits, on ='STATE', how = 'outer', indicator= True)
outer_merge
dropped_from_both = outer_merge[(outer_merge['_merge']  == 'left_only') | (outer_merge['_merge'] == 'right_only')]
dropped_from_both #Observations dropped from both the population and state-visited datasets


#Further Investigation
left_merge = pop_data_bkp.merge(state_visits, on = 'STATE', how = 'left', indicator = True)
dropped_from_population = left_merge[left_merge['_merge'] == 'left_only']
#Observations dropped from the population dataset
dropped_from_population
state_visits[state_visits['STATE'] == 'PR']


right_merge = pop_data_bkp.merge(state_visits, on = 'STATE', how = 'right', indicator = True)
dropped_from_statevisited = right_merge[right_merge['_merge'] == 'right_only']
#Observations dropped from the state-visited dataset
dropped_from_statevisited 
pop_data_bkp[pop_data_bkp['STATE'] == 'GU']



#Method 2 Question 5
#pop_data = pop_data.merge(state_visits, on ='STATE', how = 'outer', indicator= True)
#pop_data
#pop_data = pop_data[(pop_data['_merge']  != 'left_only') | (pop_data['_merge'] != 'right_only')]
#Investigations Method 2
#dropped_from_both = pop_data[(pop_data['_merge']  == 'left_only') | (pop_data['_merge'] == 'right_only')]
#dropped_from_both #Observations dropped from both the population and state-visited datasets


#Method 3, If we merge the data set from question 3
#pop_data_q3 = pop_data_q3.merge(state_visits, on ='STATE', how = 'outer', indicator= True)
#pop_data_q3
#pop_data_q3 = pop_data_q3[(pop_data_q3['_merge']  != 'left_only') | (pop_data_q3['_merge'] != 'right_only')]
#Investigations Method 2
#dropped_from_both = pop_data_q3[(pop_data_q3['_merge']  == 'left_only') | (pop_data_q3['_merge'] == 'right_only')]
#dropped_from_both #Observations dropped from both the population and state-visited datasets



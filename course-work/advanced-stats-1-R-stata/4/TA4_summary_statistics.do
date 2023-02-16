* version 13.0 of STATA
* PPHA 31202 Advanced Statistics for Data Analysis 1, Fall 2020
* Assignment 4: Analyze American Community Survey Data

* Housekeeping
* a) make sure memory is clear
* b) close the log file if open
* c) not to display more message
* d) make a log file or if one already exists, replace it. 

clear 
capture log close
set more off
log using assignment4_v1.log, replace


*load data*
* names forces STATA to recognise first line in data as as variabe names
* use the appropriate command 

insheet using "C:\Users\Kaveri\Desktop\MSCAPP\Assignment4\ppha312x2020.csv", names clear
label data "Data is from IPUMS-USA  restricted to Albuquerque,New Mexico (2018)"

*Data cleaning
* To check the data for missing values or data that doesn't make sense. We first lok at the summary of 
* all the variables in the data. 

summarize

* We see that inctot,which is total income of the individual has some negative values.
* This doesn't make sense. So, we'll filter the data to only consider income greater 
* than equal to zero 

keep if inctot >= 0

* Then we summarize the data again to check if the above change was incorporated

summarize

* As STATA cannot run any statistical analysis on string variables, we will encode
* the string variables. You do not need to do this if you are using the .dta file. 

* Starting with hispan
encode hispan, gen(hispan_cat)
encode sex, gen(sex_cat)
encode race, gen(race_cat)
encode educd, gen(educd_cat)
encode empstat, gen(empstat_cat)
encode labforce, gen(labforce_cat)


* Define a dummy variable indicating the respondent is Hispanic or not. 

codebook hispan_cat
gen is_hispanic = 1
replace is_hispanic = 0 if (hispan_cat==3)


* Limit sample to white, non-Hispanic or hispanic residents. Looking at codebook race_cat, we see that the label for White is 9

keep if (race_cat == 9 & is_hispanic == 0) | is_hispanic == 1


* Compare the educational attainment of Hispanics to white respondents.

tab edu_level is_hispanic 




 


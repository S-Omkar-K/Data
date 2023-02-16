clear 
capture log close
set more off
log using Sai_Omkar_K_PS4.log, replace

*Loading data and removing first line using names

insheet using "C:\Users\saiomkark\OneDrive - The University of Chicago\AdvStats\PS4\ppha312x2021.csv", names clear


label data "Data is from IPUMS-USA  restricted to Albuquerque,New Mexico (2018)"


*analyze the data using summarize to check for NAs etc.. 
summarize

*Inctot has negative values, which it cannot be. Hence keeping only those where inctot is greater than equal to 0 
keep if inctot>= 0


*check the data if changes are applied
summarize

*Encoding the string variables so that we can analyze them in STATA
encode hispan, gen(hispan_cat)
encode sex, gen(sex_cat)
encode race, gen(race_cat)
encode educd, gen(educd_cat)
encode empstat, gen(empstat_cat)
*encode labforce, gen(labforce_cat)
encode age, gen(age_cat)
encode uhrswork, gen(uhrswork_cat)

*Question 1, variable for if respondent is Hispanic. Variable for if respondent is African/American

codebook hispan_cat
gen is_hispanic = 1
replace is_hispanic = 0 if (hispan_cat ==3)

codebook race_cat
gen is_AfricanAmerican = 0
replace is_AfricanAmerican =1 if (race_cat == 2)



*Question 1b Limit the sample to white, non-Hispanic or African American, non-Hispanic respondents;

keep if (race_cat == 9 & is_hispanic == 0) | (is_AfricanAmerican == 1 & is_hispanic == 0) 

*Question 1c  Limit the sample to those 25 to 59 years of age;
codebook age_cat
keep if (age_cat >= 25 & age_cat <= 59)



*Question 1d  Define a binary variable indicating whether the respondent is female;
codebook sex_cat
gen is_female = 0
replace is_female = 1 if (sex_cat == 1)



*Question 1e  Create an education variable with five categories: Less than high school (including GED recipients), high school degree, some college (including associates degree), bachelor’s degree, and graduate degree;

codebook educd_cat,tab(500)
gen edu_level = ""
replace edu_level = "less than high school" if (educd_cat != 1 & educd_cat != 3 & educd_cat != 24 & educd_cat != 4 & educd_cat != 19)
replace edu_level = "some college" if (educd_cat == 1 | educd_cat == 3)
replace edu_level = "high school degree" if (educd_cat == 24)
replace edu_level = "bachelors degree" if (educd_cat == 4)
replace edu_level = "graduate degree" if (educd_cat == 19)





*Question 1f Define a dummy variable for whether the respondent is employed.

codebook empstat_cat
gen is_employed = 0 
replace is_employed = 1 if (empstat_cat == 1)



*Question 2 Compare the educational attainment of African American to white respondents.
tab race_cat
* Only African/American and whites are limited to, in the data
tab edu_level is_AfricanAmerican

* In the above table, 1 is African/American and 0 are Whites
*Sample Observation : Number of African/American with bachelors degree is 203 and Whites with bachelors degree is 603

*Another way of doing this is below, to show both frequency and percentages
tab edu_level race_cat, row



*QUestion 3 Compare the employment rate by sex for African Americans and whites.
table is_employed sex_cat race_cat, contents(freq)

*Second way of doing this is grouping by sex , gives the same result
table is_employed race_cat, by(sex_cat) row

*Question 4 Conditional on working, compare hours worked and its standard deviation by sex for African Americans and whites.

*We create a new variable which hours worked with employment condition
gen uhrswork_employed = uhrswork_cat * is_employed
table race_cat, by(is_female) contents(freq)
table race_cat, by(is_female) contents(sum uhrswork_employed)
table race_cat, by(is_female) contents(sd uhrswork_employed)
table race_cat, by(is_female) contents(mean uhrswork_employed)

*Another way of doing this using bysort, tabstat. Similar result as above
bysort is_AfricanAmerican: tabstat uhrswork_cat if is_employed==1, by(sex_cat) stat(sum mean sd skewness)

*Third way is by plotting a graph to visualize 
*total hours worked below
graph bar (sum) uhrswork_cat if is_employed ==1, over(is_AfricanAmerican) by(sex_cat)
*Mean and standar deviation
graph bar (mean) uhrswork_cat (sd) uhrswork_cat if is_employed ==1, over(is_AfricanAmerican) by(sex_cat)


*Question 5 Conditional on working, compare total income, its standard deviation, and its skewness by education and sex for African Americans and whites.

gen inctot_employed = inctot * is_employed
table edu_level race_cat, by(is_female) contents(freq)
table edu_level race_cat, by(is_female) contents(sum inctot_employed)
table edu_level race_cat, by(is_female) contents(sd inctot_employed)
table edu_level race_cat, by(is_female) contents(mean inctot_employed)

*Second way of doing this is by using bysort, tabstat
bysort is_AfricanAmerican is_female: tabstat inctot_employed if inctot != 9999999, by(edu_level) stat(sum mean sd skewness)

*Third way is by plotting a graph and visualize
graph bar (mean) uhrswork_cat (sd) uhrswork_cat if is_employed ==1, over(is_AfricanAmerican) by(edu_level sex_cat)



*Question 6 For those with positive wages, compare the wage income, its standard deviation, and its skewness by education and sex for African Americans and whites.

table edu_level race_cat, by(is_female) contents(freq)
table edu_level race_cat, by(is_female) contents(sum incwage)
table edu_level race_cat, by(is_female) contents(sd incwage)
table edu_level race_cat, by(is_female) contents(mean incwage)

*The above gives abnormal results due to the incwage values of 999999 present in the data. We can use bysort function to exclude them from the analysis
bysort is_AfricanAmerican is_female: tabstat incwage if incwage != 999999, by(edu_level) stat(sum mean sd skewness)


*Question 7 Calculate employment rates by age and sex for African Americans and whites.
table age_cat race_cat, by(is_female) contents(freq)
table age_cat race_cat, by(is_female) contents(mean is_employed)
table age_cat race_cat, by(is_female) contents(sd is_employed)
*Second way to do this is by using bysort, tabstat
bysort is_AfricanAmerican is_female : tabstat is_employed, by(age_cat) stat(sum mean sd skewness)


*Question 8 Conditional on working, compare the hours worked by education and sex for African Americans and whites.

table edu_level race_cat, by(is_female) contents(freq)
table edu_level race_cat, by(is_female) contents(sum uhrswork_employed)
table edu_level race_cat, by(is_female) contents(mean uhrswork_employed)
table edu_level race_cat, by(is_female) contents(sd uhrswork_employed)



log close

translate Sai_Omkar_K_PS4.log Sai_Omkar_K_PS4.pdf




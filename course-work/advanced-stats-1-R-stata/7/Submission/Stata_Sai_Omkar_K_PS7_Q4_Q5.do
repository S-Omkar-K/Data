clear 
capture log close
set more off
log using Sai_Omkar_K_PS7_Q4_Q5.log, replace

*Loading data and removing first line using names

use "C:\Users\saiomkark\OneDrive - The University of Chicago\AdvStats\PS7\Homework_7.dta"




*analyze the data using summarize to check for NAs etc.. 
summarize

*Inctot has negative values, which it cannot be. Hence keeping only those where inctot is greater than equal to 0 
keep if inctot>= 0


*check the data if changes are applied
summarize

*filtering data to required age

keep if age >= 25 & age <= 55

* Divide people into six educational categories: 1) less than high school including GED recipients. 2) exactly a high school degree. 3) some college but no degree 4) associates degree 5) exactly bachelors degree 6) more than a bachelors degree.

codebook educd,tab(25)
gen edu_cat = "less than high school including GED recipients"
replace edu_cat = "exactly a high school degree" if educd == 63
replace edu_cat = "some college but no degree" if educd == 64 | educd == 65 | educd == 71
replace edu_cat = "associates degree" if educd == 81
replace edu_cat = "exactly bachelor’s degree" if educd == 101
replace edu_cat = "more than a bachelor’s degree" if educd == 114 | educd == 115 | educd == 116
br edu_cat educd


*Arranging the data according to the racial groups into White -> 1, African American -> 2, Other -> 3
gen race_cat = "Other race"
replace race_cat = "White" if (race == 1)
replace race_cat = "African American" if (race == 2)
br race_cat race


*check the data if changes are applied
summarize

*Question 4A - A Calculate the income from wages and salaries for those with positive earn-ings by sex and race;

tab sex race_cat, sum(inctot)

*Question 4B Calculate the income from wages and salaries for those with positive earn-ings by sex and race using the weights “perwt.”

tab sex race_cat [aw=perwt], sum(inctot)


***********************************************************************************



*Question 5 5. Use the same data set and setup as in problem 4. Create an age category variable with categories, 25 −29, 30 −34, 35 −39, 40 −44, 45 −49, and 50 −55. The variable “qincwage” is equal to four when the data are suppressed. Using our race, age, sex, and education categories along with the sample weights, construct IPW weights to account for the imputed income. Calculate income from wages and salaries by sex and race using the IPW weights. Compare these means to those in problem 4b.



egen age_cat = cut(age), at(25,30,35,40,45,50,56)


*
* Construct missing indicator for income
*
gen miss = qinctot == 4
* construct phat
*
* creates a unique variable for each age, sex  and education category
*
egen x = group(age_cat sex edu_cat)
*
* total people in each sex by age and education categories
*
egen den = sum(perwt), by(x)
*
* people with non-missing data
*
egen num =  sum((1-miss)*perwt), by(x)
*
* probability of responding
gen phat = num/den
*
* generate new weights called "wt".  Again, note the use of perwts.
*
gen wt = perwt/phat if miss == 0
*
* Test to make sure weights work.  Fraction by age_cat should be the same
*
* using perwt
tab age_cat [aw=perwt]
* using our new wts
tab age_cat [aw=wt]
* Test to make sure weights work.  Fraction by sex should be the same
*
* using perwt
tab sex [aw=perwt]

tab sex [aw=perwt], summarize(incwage)
* using our new wts
tab sex [aw=wt]

*


* Test to make sure weights work.  Fraction by edu_cat should be the same
*
* using perwt
tab edu_cat [aw=perwt]
* using our new wts
tab edu_cat [aw=wt]

*Comparing total income with old weights and total income with new weights derived

tab sex [aw=perwt], sum(inctot)
tab sex [aw=wt], sum(inctot)
tab sex race_cat [aw = perwt], summarize(incwage)
tab sex race_cat [aw=wt], summarize(incwage)

*The means are lower using IPW weights than using "perwt". Almost similar, but not close


log close

translate Sai_Omkar_K_PS7_Q4_Q5.log Sai_Omkar_K_PS7_Q4_Q5.pdf

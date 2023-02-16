clear 
capture log close
set more off
log using Stata_Sai_Omkar_K_PS7_Q1.log, replace

*Loading data and removing first line using names

insheet using "C:\Users\saiomkark\OneDrive - The University of Chicago\AdvStats\PS7\ppha312x2021.csv", names clear


label data "Data is from IPUMS-USA  restricted to Albuquerque,New Mexico (2018)"
*use ppha312x2021

*analyze the data using summarize to check for NAs etc.. 
summarize

*Inctot has negative values, which it cannot be. Hence keeping only those where inctot is greater than equal to 0 
keep if inctot>= 0


*check the data if changes are applied
summarize

*Encoding the string variables so that we can analyze them in STATA

encode sex, gen(sex_cat)
encode race, gen(race_cat)
encode empstat, gen(empstat_cat)
encode age, gen(age_cat)



codebook race_cat
gen is_AfricanAmerican = 0
replace is_AfricanAmerican =1 if (race_cat == 2)

codebook sex_cat
gen is_female = 0
replace is_female = 1 if (sex_cat == 1)

codebook empstat_cat
gen is_employed = 0 
replace is_employed = 1 if (empstat_cat == 1)

*limiting the sample to African American Women respondents, who are employed 
keep if (is_employed == 1 & is_female == 1 & is_AfricanAmerican == 1)

*Using bootstrap to determine standard error of the correlation coefficient between wages and worker ages. 10000 replications with seed 110821

drop if age_cat == .
drop if incwage == .

bootstrap r(rho), nodots nowarn seed(110821) reps(10000): correlate incwage age_cat

log close

translate Stata_Sai_Omkar_K_PS7_Q1.log Stata_Sai_Omkar_K_PS7_Q1.pdf
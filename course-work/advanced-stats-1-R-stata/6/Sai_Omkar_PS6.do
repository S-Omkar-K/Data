*Sai Omkar PS - 6

clear 
capture log close
set more off
log using Sai_Omkar_PS6.log, replace
*
* clear memory in stata
*
clear

insheet using "C:\Users\saiomkark\OneDrive - The University of Chicago\AdvStats\PS6\ppha312x2021.csv", names clear
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
summarize 


* variable for if respondent is Hispanic. Variable for if respondent is African/American

codebook hispan_cat
gen is_hispanic = 1
replace is_hispanic = 0 if (hispan_cat == 3)

codebook race_cat
gen is_AfricanAmerican = 0
replace is_AfricanAmerican = 1 if (race_cat == 2)


*Limit the sample to white, non-Hispanic or African American, non-Hispanic respondents;
keep if (race_cat == 9 & is_hispanic == 0) | (is_AfricanAmerican == 1 & is_hispanic == 0)


*Variable indicating whether the respondent is female
codebook sex_cat
gen is_female = 0
replace is_female = 1 if (sex_cat == 1)

* Limit the age [25:55]
codebook age_cat
keep if (age_cat >= 25 & age_cat <= 55) & is_female == 1

* Dummy variable for whether the respondent is employed.
codebook empstat_cat
gen is_employed = 0
replace is_employed = 1 if (empstat_cat == 1) 

*3: Using data from Homework 4, test the hypothesis that African American women and white women ages 25-55 (inclusive) have the same probability of being employed. Use a two-sided Fisher’s exact test and a chi-square test with a 95% confidence level
bysort is_AfricanAmerican: tabstat is_employed, stat(count sum)

* Null hypothesis: Hn: Probability of being employed is same for white women and African American women ages 25-55 (inclusive))
* Alternative hypothesis: Ha: Probability of being employed is not same, greater for white women than that of African American women ages 25-55 (inclusive)

* Fisher's test: 
cci 791 264 599 202, exact

* Observations: 
* African American women and white women ages [25:55] have the same probability of being employed. The p-value = 0.9569  for two-tail test and The p-value = 0.4828 for the one-tail test are greater than 0.05. Thus the Null Hypothesis is not rejected. 

* chi-square test: 
tabi 791 264 \ 599 202, chi2

* Observations: 
*African American women and white women ages [25:55] have the same probability of being employed. The p-value = 0.924 for the test is greater than 0.05. Thus the Null Hypothesis cannot rejected. 


* Question 4: Using data from Homework 4, test the hypothesis that African American women and white women ages 25-55 (inclusive) have the same total income. Use a two-sided t-test with a 95% confidence level. How confident of this test are you? Why?
gen inc_tot_employed = inctot * is_employed*is_AfricanAmerican*is_female
ttest inc_tot_employed, by(is_AfricanAmerican) unequal level(95) welch

* Observations for two-sided t-test:
* P-value = 0 for  two-sided t-test with a 95% confidence level is less than 0.05. Thus the Null hypothesis that true difference in means of total income is equal to 0 between white women and African/American women ages [25:55] can be rejected. The Alternative Hypothesis that true difference in means of total income is not 0 between white women and African American women ages [25:55] cannot be rejected.

*Similarly, for difference in mean (White - African/American) is "less" than zero. We got P =1 with 95% confidence level which is greater than 0.05. Thus we can reject the alternate hypotheses that the true difference in mean of total income between White women and African/American women with age range [25:55] is less than zero can be rejected. Null hypotheses that true difference in the above said mean is zero cannot be rejected.

*Similarly, the alternate hypotheses that difference in mean of total income for White women and African/American women with age range [25:55] is greater than 0 cannot be rejected because of the p-value = 0 for 95% confidence level , which is less than 0.05. Also, due to the p value we can reject the null hypotheses that the true difference of the above said mean can be rejected. 


* Looking at the above p values in different observances, the hypotheses that the the mean of total income of White women is greater than the African/American women with age ranges [25-55] cannot be rejected.



log close

translate Sai_Omkar_PS6.log Sai_Omkar_PS6_Stata.pdf
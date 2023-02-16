/* This program was written 11/30/2021 by Dan Black for an example of IPW weights for PPHA 312.

Will use whites, 25-55 years old, and use age and sex as the covariates for total income.
 
 
*/
*
*
*
* 
clear all
set more off
capture log close
log using crIPW.log, replace
use Homework_7.dta
*
* keep whites
*
keep if race == 1
*
* keep those 25 to 55, inclusive
*
keep if age > 24 & age < 56
*
* Construct missing indicator for income
*
gen miss = qinctot == 4
*
* construct phat
*
* creates a unique variable for each age and sex category
*
egen x = group(age sex)
*
* total people in each sex by age category (used perwts: see why?)
*
egen den = sum(perwt), by(x)
*
* people with non-missing data
*
egen num = sum((1-miss)*perwt), by(x)
*
* probability of responding
gen phat = num/den
*
* generate new weights called "wt".  Again, note the use of perwts.
*
gen wt = perwt/phat if miss == 0
*
* Test to make sure weights work.  Fraction by age should be the same
*
* using perwt
tab age [aw=perwt]
* using our new wts
tab age [aw=wt]
*
* Test to make sure weights work.  Fraction by sex should be the same
*
* using perwt
tab sex [aw=perwt]
* using wt
tab sex [aw=wt]
*
* Now compare the total income with old and new weights.  These should differ a bit
*
tab sex [aw=perwt], sum(inctot)
tab sex [aw=wt], sum(inctot)
* end
log close




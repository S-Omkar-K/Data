clear

capture log close
set more off

log using ProblemSet.log, replace

set seed 10072021
set obs 100

*In this example, we have a 3-sided die where:
*The probability of rolling a 1 is 0.25
*The probability of rolling a 2 is 0.3
*The probability of rolling a 3 is 0.45

*Generate random number p1 between 0 and 1
generate p1 = runiform()


*Generate x1 value from random number p1
generate x1 = 1 if p1 <= 1/15
replace x1 = 2 if p1 <= 3/15 & p1 > 1/15
replace x1 = 3 if p1 <= 6/15 & p1 > 3/15
replace x1 = 4 if p1 <= 10/15 & p1 > 6/15
replace x1 = 5 if p1 <= 1 & p1 > 10/15

*Calculate mean and standard deviation , varuiance from simulation
sum x1, detail




log close
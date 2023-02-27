* version 16.1 of STATA
* PPHA 31202 Advanced Statistics for Data Analysis 1, Fall 2021

* Housekeeping
* a) make sure memory is clear
* b) close the log file if open
* c) not to display more message
* d) make a log file or if one already exists, replace it. 

clear 
capture log close
set more off
log using HW5_example2.log, replace


*Question 1: (20 points) You wish to test the hypothesis that a coin is fair and you have
* data from 9 coin flips. Use an exact test.
*       A. Describe the results that would allow you to accept and reject the null
*          hypothesis of a fair coin with a two-sided test at the 95% confidence level;
*       B. Describe the results that would allow to you accept and reject the null
*          hypothesis of a fair coin with a one-sided test at the 95% confidence level
*          (with the alternate hypothesis being that the probability of getting heads
*          is greater than 0.5).
 
 
forvalues i = 0(1)9{ 
	bitesti 9 `i' 0.5
	}



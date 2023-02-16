*
* Simple bootstrap program
*
capture log close
clear
log using L7bootstrap.log, replace
cd ""
*
* 1) one sample, using "bootstrap standard error for the 25th percentile"
*
* open dta file, need another function if opening cvs file
use onesample
* drop missing data
drop if x == .
* get summary statistics of x in detail
sum x, d
* bootstrap for the 25th percentile, no replication dot displaying & no warn displaying & set seed for simulation & b = 10,000 & saving results in "onettest": using one sample t-test command
bootstrap r(p25), nodots seed(110821) reps(10000): summarize x, d
*
* 2) one sample, using "bootstrap t-statistic"
*
* one sample t-test with a mean of 35 on existing "onesample" 
ttest x == 35
* bootstrap for t-statistic, no replication dot displaying & no warn displaying & set seed for simulation & b = 10,000 & saving results in "onettest": using one sample t-test command
bootstrap r(t), nodots nowarn seed(110821) reps(10000) saving(onettest,replace): ttest x == 35
* clear the data editor
clear
* use results that stored in "onettest"
use onettest
* get the 2.5 percentile and 97.5 percentile t-statistic
centile _bs_1, c(2.5, 97.5)
*
* 3) two sample, using "bootstrap standard error for correlation coefficient"
*
* clear the data editor
clear
* open dta file, need another function if opening cvs file
use twosample
* get summary statistics of math within different fem groups
tab fem, sum(math)
* drop missing data
drop if math == .
drop if fem == .
* bootstrap for correlation coefficient of math and fem
bootstrap r(rho), nodots nowarn seed(110821) reps(10000): correlate math fem
*
log close

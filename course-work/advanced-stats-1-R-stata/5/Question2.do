*Sai Omkar Kandukuri PS5 Q2

clear 
capture log close
set more off
log using Question2.log, replace

clear
*For this exercise, you will use a simulation to see how well the CLT works with finite samples in R. Parts (a) and (b) of this question each describe a distribution. For each distribution, use 10,000 draws using each of the following sample sizes: n = 36, n = 64, n = 100, n = 225, n = 2500, and n = 12100. Then discuss how well the normal approximation fits your simulated estimates of the means at the critical values of 0.025 and 0.975.
* a) Suppose that x is binary with Pr(x = 1) = 0.35.
* b) Suppose that x is binary with Pr(x = 1) = 0.97


capture program drop clt
program clt, rclass
version 15.0




args N
clear

*
*
quietly set obs `N'
*
*
tempvar y1 y2
*
* y1 is binary with Pr(y1=1) = 0.35
*
gen `y1' = uniform() < 0.35
*
* y2 is binary with Pr(y1=1) = 0.97
*
gen `y2' = uniform() < 0.97
*
*
quietly sum `y1'
*
*
return scalar mu1 = r(mean)
return scalar sd1 = r(sd)
*
*
quietly sum `y2'
*
*
return scalar mu2 = r(mean)
return scalar sd2 = r(sd)
*
*
end
*
*
set seed 24031997

*
*
simulate mu1 = r(mu1) mu2 = r(mu2) sd1 = r(sd1) sd2 = r(sd2), reps(10000) nodots: clt 36
*
*
save clt36, replace
*
* Sample of 36 observations
*
use clt36
gen z1 = (mu1-0.35)      /(sd1/36^(1/2))
gen z2 = (mu2-0.97)      /(sd2/36^(1/2))

*
*
gen rrej1 = z1 >  1.96 & z1 < .
gen lrej1 = z1 < -1.96
gen rrej2 = z2 >  1.96 
gen lrej2 = z2 < -1.96
*
*
sum rrej1-lrej2 

bitest lrej1 = 0.025 
bitest rrej1 = 0.025
bitest lrej2 = 0.025
bitest rrej2 = 0.025


replace rrej1 = z1 >  0.975 & z1 < .
replace lrej1 = z1 < -0.975
replace rrej2 = z2 >  0.975 
replace lrej2 = z2 < -0.975

*0.175
*
sum rrej1-lrej2

bitest lrej1 = 0.175 
bitest rrej1 = 0.175
bitest lrej2 = 0.175
bitest rrej2 = 0.175


replace rrej1 = z1 >  0.025 & z1 < .
replace lrej1 = z1 < -0.025
replace rrej2 = z2 >  0.025 
replace lrej2 = z2 < -0.025

*0.5
*
sum rrej1-lrej2

bitest lrej1 = 0.50 
bitest rrej1 = 0.50
bitest lrej2 = 0.50
bitest rrej2 = 0.50


clear

*
*
simulate mu1 = r(mu1) mu2 = r(mu2) sd1 = r(sd1) sd2 = r(sd2), reps(10000) nodots: clt 64
*
* save this data
*
save clt64, replace
*
* Sample using 64 observations
*
use clt64
gen z1 = (mu1-0.35)      /(sd1/64^(1/2))
gen z2 = (mu2-0.97)      /(sd2/64^(1/2))

*
* construct rejection level 5 percent rate; left and right tails
*
gen rrej1 = z1 >  1.96 & z1 < .
gen lrej1 = z1 < -1.96
gen rrej2 = z2 >  1.96 
gen lrej2 = z2 < -1.96
*
* Should be 0.05, 1 binary 2 binary
*
sum rrej1-lrej2 // 64 observations
/*
99% (-1%)  2.33
95% (-5%)  1.65
90% (-10%) 1.29
75% (-25%) 0.58
*/
bitest lrej1 = 0.025 
bitest rrej1 = 0.025
bitest lrej2 = 0.025
bitest rrej2 = 0.025


replace rrej1 = z1 >  0.975 & z1 < .
replace lrej1 = z1 < -0.975
replace rrej2 = z2 >  0.975 
replace lrej2 = z2 < -0.975

*
* Should be around 0.175
*
sum rrej1-lrej2

bitest lrej1 = 0.175 
bitest rrej1 = 0.175
bitest lrej2 = 0.175
bitest rrej2 = 0.175


replace rrej1 = z1 >  0.025 & z1 < .
replace lrej1 = z1 < -0.025
replace rrej2 = z2 >  0.025 
replace lrej2 = z2 < -0.025

*
* Should be 0.50
*
sum rrej1-lrej2

bitest lrej1 = 0.50 
bitest rrej1 = 0.50
bitest lrej2 = 0.50
bitest rrej2 = 0.50


clear
*
*  run simulation for 100 observations
*
simulate mu1 = r(mu1) mu2 = r(mu2) sd1 = r(sd1) sd2 = r(sd2), reps(10000) nodots: clt 100
*
* save this data
*
save clt100, replace
*
* Sample using 100 observations
*
use clt100
gen z1 = (mu1-0.35)      /(sd1/100^(1/2))
gen z2 = (mu2-0.97)      /(sd2/100^(1/2))

*
* construct rejection level 5 percent rate; left and right tails
*
gen rrej1 = z1 >  1.96 & z1 < .
gen lrej1 = z1 < -1.96
gen rrej2 = z2 >  1.96 
gen lrej2 = z2 < -1.96
*
* Should be 0.05, 1 binary 2 binary
*
sum rrej1-lrej2 // 100 observations
/*
99% (-1%)  2.33
95% (-5%)  1.65
90% (-10%) 1.29
75% (-25%) 0.58
*/

bitest lrej1 = 0.025 
bitest rrej1 = 0.025
bitest lrej2 = 0.025
bitest rrej2 = 0.025


replace rrej1 = z1 >  0.975 & z1 < .
replace lrej1 = z1 < -0.975
replace rrej2 = z2 >  0.975 
replace lrej2 = z2 < -0.975

*
* Should be around 0.175
*
sum rrej1-lrej2

bitest lrej1 = 0.175 
bitest rrej1 = 0.175
bitest lrej2 = 0.175
bitest rrej2 = 0.175


replace rrej1 = z1 >  0.025 & z1 < .
replace lrej1 = z1 < -0.025
replace rrej2 = z2 >  0.025 
replace lrej2 = z2 < -0.025

*
* Should be 0.50
*
sum rrej1-lrej2

bitest lrej1 = 0.50 
bitest rrej1 = 0.50
bitest lrej2 = 0.50
bitest rrej2 = 0.50


clear

*
*  run simulation for 225 observations
*
simulate mu1 = r(mu1) mu2 = r(mu2) sd1 = r(sd1) sd2 = r(sd2), reps(10000) nodots: clt 225
*
* save this data
*
save clt225, replace
*
* Sample using 225 observations
*
use clt225
gen z1 = (mu1-0.35)      /(sd1/225^(1/2))
gen z2 = (mu2-0.97)      /(sd2/225^(1/2))

*
* construct rejection level 5 percent rate; left and right tails
*
gen rrej1 = z1 >  1.96 & z1 < .
gen lrej1 = z1 < -1.96
gen rrej2 = z2 >  1.96 
gen lrej2 = z2 < -1.96
*
* Should be 0.05, 1 binary 2 binary
*
sum rrej1-lrej2 // 225 observations
/*
99% (-1%)  2.33
95% (-5%)  1.65
90% (-10%) 1.29
75% (-25%) 0.58
*/

bitest lrej1 = 0.025 
bitest rrej1 = 0.025
bitest lrej2 = 0.025
bitest rrej2 = 0.025


replace rrej1 = z1 >  0.975 & z1 < .
replace lrej1 = z1 < -0.975
replace rrej2 = z2 >  0.975 
replace lrej2 = z2 < -0.975

*
* Should be around 0.175
*
sum rrej1-lrej2

bitest lrej1 = 0.175 
bitest rrej1 = 0.175
bitest lrej2 = 0.175
bitest rrej2 = 0.175


replace rrej1 = z1 >  0.025 & z1 < .
replace lrej1 = z1 < -0.025
replace rrej2 = z2 >  0.025 
replace lrej2 = z2 < -0.025

*
* Should be 0.50
*
sum rrej1-lrej2

bitest lrej1 = 0.50 
bitest rrej1 = 0.50
bitest lrej2 = 0.50
bitest rrej2 = 0.50


clear

*
*  run simulation for 2500 observations
*
simulate mu1 = r(mu1) mu2 = r(mu2) sd1 = r(sd1) sd2 = r(sd2), reps(10000) nodots: clt 2500
*
* save this data
*
save clt2500, replace
*
* Sample using 2500 observations
*
use clt2500
gen z1 = (mu1-0.35)      /(sd1/2500^(1/2))
gen z2 = (mu2-0.97)      /(sd2/2500^(1/2))

*
* construct rejection level 5 percent rate; left and right tails
*
gen rrej1 = z1 >  1.96 & z1 < .
gen lrej1 = z1 < -1.96
gen rrej2 = z2 >  1.96 
gen lrej2 = z2 < -1.96
*
* Should be 0.05, 1 binary 2 binary
*
sum rrej1-lrej2 // 2500 observations
/*
99% (-1%)  2.33
95% (-5%)  1.65
90% (-10%) 1.29
75% (-25%) 0.58
*/
bitest lrej1 = 0.025 
bitest rrej1 = 0.025
bitest lrej2 = 0.025
bitest rrej2 = 0.025


replace rrej1 = z1 >  0.975 & z1 < .
replace lrej1 = z1 < -0.975
replace rrej2 = z2 >  0.975 
replace lrej2 = z2 < -0.975

*
* Should be around 0.175
*
sum rrej1-lrej2

bitest lrej1 = 0.175 
bitest rrej1 = 0.175
bitest lrej2 = 0.175
bitest rrej2 = 0.175


replace rrej1 = z1 >  0.025 & z1 < .
replace lrej1 = z1 < -0.025
replace rrej2 = z2 >  0.025 
replace lrej2 = z2 < -0.025

*
* Should be 0.50
*
sum rrej1-lrej2

bitest lrej1 = 0.50 
bitest rrej1 = 0.50
bitest lrej2 = 0.50
bitest rrej2 = 0.50

clear

*
*  run simulation for 12100 observations
*
simulate mu1 = r(mu1) mu2 = r(mu2) sd1 = r(sd1) sd2 = r(sd2), reps(10000) nodots: clt 12100
*
* save this data
*
save clt12100, replace
*
*
* Sample using 12100 observations
*
use clt12100
gen z1 = (mu1-0.35)	     /(sd1/12100^(1/2))
gen z2 = (mu2-0.97)      /(sd2/12100^(1/2))

*
* construct rejection level 5 percent rate; left and right tails
*
gen rrej1 = z1 >  1.96 & z1 < .
gen lrej1 = z1 < -1.96
gen rrej2 = z2 >  1.96 
gen lrej2 = z2 < -1.96
*
* Should be 0.05
*
sum rrej1-lrej2 // 12100 observations

bitest lrej1 = 0.025 
bitest rrej1 = 0.025
bitest lrej2 = 0.025
bitest rrej2 = 0.025


replace rrej1 = z1 >  0.975 & z1 < .
replace lrej1 = z1 < -0.975
replace rrej2 = z2 >  0.975 
replace lrej2 = z2 < -0.975

*
* Should be around 0.175
*
sum rrej1-lrej2

bitest lrej1 = 0.175 
bitest rrej1 = 0.175
bitest lrej2 = 0.175
bitest rrej2 = 0.175


replace rrej1 = z1 >  0.025 & z1 < .
replace lrej1 = z1 < -0.025
replace rrej2 = z2 >  0.025 
replace lrej2 = z2 < -0.025

*
* Should be 0.50
*
sum rrej1-lrej2

bitest lrej1 = 0.50 
bitest rrej1 = 0.50
bitest lrej2 = 0.50
bitest rrej2 = 0.50

clear


*Observations
*Central Limit theorem is interpreted here.
*1. As we increase N, the percentage of sample means that have a z-score below -0.025 and above 0.025 is ~99%.
*2. For critical point z = 0.975: As we increase N, the percentage of sample means that have a z-score below -0.975 and above 0.975 is ~34%, which means 66% of the sample means are between z score of 0.975.
*These simulation results are in accordance with a typical normal distribution where almost 68% of sample means lie within a z-score of 1 and where many sample means fall outside the z-score of 0.025 as the interval defined by the same is very very small. 



*
* close log file
*
log close


translate Question2.log Question2.pdf
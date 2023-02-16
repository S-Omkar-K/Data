*Sai Omkar Kandukuri PS5 Q3



clear 
capture log close
set more off
log using Question3.log, replace
*
* clear memory in stata
*
clear
*
*Use Stata in this exercise. Suppose that x is drawn from the following “mixing distribution.” Let y be a binary random variable with Pr(y = 1) = 0.9. If y = 1, then x is drawn from a standard normal distribution. If y = 0, then x is drawn from a normal distribution with μ = 100 and standard deviation σ = 20.
* a) Find the mean of x.
* b) For this distribution, use 10,000 draws from each of the following sample sizes: n = 36, n = 64, n = 100, n = 225, n = 2500, and n = 12100. Discuss how well the normal approximation fits your simulated estimates of the mean at the critical values of 0.025 and 0.975.


set seed 10072021
set obs 100000
* y is binary with Pr(y1=1) = 0.9
*
gen y = runiform() < 0.9
sum y
*
* If y = 1, then x is drawn from a standard normal distribution. If y = 0, then x is drawn from a normal distribution with μ = 100 and standard deviation σ = 20
*
gen x = rnormal() if (y == 1)
replace x = rnormal(100, 20) if (y == 0)
sum x

clear

*
* In case the program "clt" is resident in memory drop it because we will redefine it in this program.  Capture simply tells stata to ignore this command if the "clt" is not in memory
*
capture program drop clt
*
* define program.  This is the program that we will 10,000 times for each sample size; rclass tells us that we will be using results stored in the class r() 
*
program clt, rclass
version 15.0
*
* Simulations for central limit theorem (clt)
*
* declare argument of program; only one in this program the sample size
*
args N
*
* clear any variables in memory
*
clear
*
* set observations to `N'. "quietly" tells stata not to put the results on your screen
*
quietly set obs `N'
*
* Set temporary variables.  Temporary variables are dropped whenever we start a new "loop" through the data
*
tempvar y x
*
* y is binary with Pr(y1=1) = 0.9
*
gen `y' = uniform() < 0.9
*
* If y = 1, then x is drawn from a standard normal distribution. If y = 0, then x is drawn from a normal distribution with μ = 100 and standard deviation σ = 20
*
gen `x' = rnormal() if (`y' == 1)
replace `x' = rnormal(100, 20) if (`y' == 0)

*
* calculate means and standard deviation; "quietly" command suppresses output
*
quietly sum `y'
*
* return scalar mu"y" recovers the mean sd the standard deviation
*
return scalar muy = r(mean)
return scalar sdy = r(sd)
*
* calculate means and standard deviation; "quietly" command suppresses output
*
quietly sum `x'
*
* return scalar mu"x" recovers the mean sd the standard deviation
*
return scalar mux = r(mean)
return scalar sdx = r(sd)
*
* end the program definition
*
end
*
* Set out seed
*
set seed 24031997

*
* run simulation for 36 observations
*
simulate muy = r(muy) mux = r(mux) sdy = r(sdy) sdx = r(sdx), reps(10000) nodots: clt 36
*
* save this data
*
save clt36, replace
*
* Sample using 36 observations
*
use clt36
gen z1 = (muy-0.9)      /(sdy/36^(1/2))
gen z2 = (mux-10)      /(sdx/36^(1/2))

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
sum rrej1-lrej2 // 36 observations
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
* Should be around 0.175 given that ~35% of sample means remain outliers at z = 1 (~ 17.5% on each side) for a normal distribution
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
*
* Should be around 0.50 on each side given that value of z is low at 0.025. Most sample means should fall as outliers for this range.
*
bitest lrej1 = 0.50 
bitest rrej1 = 0.50
bitest lrej2 = 0.50
bitest rrej2 = 0.50

clear

*
*  run simulation for 64 observations
*
simulate muy = r(muy) mux = r(mux) sdy = r(sdy) sdx = r(sdx), reps(10000) nodots: clt 64
*
* save this data
*
save clt64, replace
*
* Sample using 64 observations
*
use clt64
gen z1 = (muy-0.9)      /(sdy/64^(1/2))
gen z2 = (mux-10)      /(sdx/64^(1/2))

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
* Should be around 0.175 given that ~35% of sample means remain outliers at z = 1 (~ 17.5% on each side) for a normal distribution
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

*
* Should be around 0.50 on each side given that value of z is low at 0.025. Most sample means should fall as outliers for this range.
*

bitest lrej1 = 0.50 
bitest rrej1 = 0.50
bitest lrej2 = 0.50
bitest rrej2 = 0.50

clear
*
*  run simulation for 100 observations
*
simulate muy = r(muy) mux = r(mux) sdy = r(sdy) sdx = r(sdx), reps(10000) nodots: clt 100
*
* save this data
*
save clt100, replace
*
* Sample using 100 observations
*
use clt100
gen z1 = (muy-0.9)      /(sdy/100^(1/2))
gen z2 = (mux-10)      /(sdx/100^(1/2))
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
* Should be around 0.175 given that ~35% of sample means remain outliers at z = 1 (~ 17.5% on each side) for a normal distribution
*
sum rrej1-lrej2

bitest lrej1 = 0.175 
bitest rrej1 = 0.175
bitest lrej2 = 0.175
bitest rrej2 = 0.175

*
* Should be around 0.50 on each side given that value of z is low at 0.025. Most sample means should fall as outliers for this range.
*

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
simulate muy = r(muy) mux = r(mux) sdy = r(sdy) sdx = r(sdx), reps(10000) nodots: clt 225
*
* save this data
*
save clt225, replace
*
* Sample using 225 observations
*
use clt225
gen z1 = (muy-0.9)      /(sdy/225^(1/2))
gen z2 = (mux-10)      /(sdx/225^(1/2))

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
* Should be around 0.175 given that ~35% of sample means remain outliers at z = 1 (~ 17.5% on each side) for a normal distribution
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
* Should be around 0.50 on each side given that value of z is low at 0.025. Most sample means should fall as outliers for this range.
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
simulate muy = r(muy) mux = r(mux) sdy = r(sdy) sdx = r(sdx), reps(10000) nodots: clt 2500
*
* save this data
*
save clt2500, replace
*
* Sample using 2500 observations
*
use clt2500
gen z1 = (muy-0.9)      /(sdy/2500^(1/2))
gen z2 = (mux-10)      /(sdx/2500^(1/2))

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
* Should be around 0.175 given that ~35% of sample means remain outliers at z = 1 (~ 17.5% on each side) for a normal distribution
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
* Should be around 0.50 on each side given that value of z is low at 0.025. Most sample means should fall as outliers for this range.
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
simulate muy = r(muy) mux = r(mux) sdy = r(sdy) sdx = r(sdx), reps(10000) nodots: clt 12100
*
* save this data
*
save clt12100, replace
*
*
* Sample using 12100 observations
*
use clt12100
gen z1 = (muy-0.9)      /(sdy/12100^(1/2))
gen z2 = (mux-10)      /(sdx/12100^(1/2))

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
sum rrej1-lrej2 // 12100 observations
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
* Should be around 0.175 given that ~35% of sample means remain outliers at z = 1 (~ 17.5% on each side) for a normal distribution
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
* Should be around 0.50 on each side given that value of z is low at 0.025. Most sample means should fall as outliers for this range.
*
sum rrej1-lrej2

bitest lrej1 = 0.50 
bitest rrej1 = 0.50
bitest lrej2 = 0.50
bitest rrej2 = 0.50

clear


*Observations
*Central Limit theorem is interpreted here.
*a)Mean of the random variable 'x' following the 'Mixed distribution' = 10
*b)
*1. As we increase N, the percentage of sample means that have a z-score below -0.025 and above 0.025 is ~99%.
*2. For critical point z = 0.975: As we increase N, the percentage of sample means that have a z-score below -0.975 and above 0.975 is ~34%, which means 66% of the sample means are between z score of 0.975.
*These simulation results are in accordance with a typical normal distribution where almost 68% of sample means lie within a z-score of 1 and where many sample means fall outside the z-score of 0.025 as the interval defined by the same is very very small. 



*
* close log file
*
log close

translate Question3.log Question3.pdf
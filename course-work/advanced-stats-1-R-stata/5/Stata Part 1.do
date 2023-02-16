*
* This program is written for PP 312 to show students how to write a do file in Stata
* for doing Monte Carlo simulations. We run 10,000 simulations for each of sample size of
* 10, 20, 30, 50, 200, 500, and 2000.  We save the relevant data sets
*
* close any open log file. capture tells stata to ignore command if no log file is open
capture log close
* 
* Written by Dan Black on 11-01-2010
*
log using crsimCLT.log, replace
*
* clear memory in stata
*
clear
*
* In case the program "clt" is resident in memory drop it because we will redefine it in this program.  Caapture simly tells stata to ignore
* this command if the "clt" is not in memory
*
capture program drop clt
*
* define program.  This is the program that we will 10,000 times for each sample size; rclass tells us that we 
* be using results stored in the class r() (as opposed to e() or s() )
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
tempvar y1 y2 y3 y4 y5 y6
*
* generate the raw data
*
*
* y6 will be used for y5, simply programming.  It is U[0,1]
*
gen `y6' = uniform()
*
* y1 is binary with Pr(y1=1) = 0.89
*
gen `y1' = uniform() < 0.89
*
* Exponential distribution with mean 10 and sd (10)
*
gen `y2' = invexponential(10,uniform())
*
* Log normal distribution with with mean exp(1+1/2) (about 4.48) and sd (exp(2*(1+1)) - exp(2+1))^1/2 (about 5.87 )
*
gen `y3' = exp(1 + 1*invnorm(uniform()))
*
* Laplace distribution with mean 10 and sd (18)^0.5 or 4.24
*
gen `y4' = invlaplace(10,3,uniform())
*
* Our U-shaped distribution, mean 0 and variance .6 or sd of about .77; "quietly" command suppresses output
*
quietly gen `y5' = (2*`y6' - 1)^(1/3) if (2*`y6' - 1) >=0
quietly replace `y5' = - (abs(2*`y6' - 1))^(1/3) if (2*`y6' - 1) < 0
*
* calculate means and standard deviation; "quietly" command suppresses output
*
quietly sum `y1'
*
* return scalar mu"x" recovers the mean sd the standard deviation
*
return scalar mu1 = r(mean)
return scalar sd1 = r(sd)
quietly sum `y2'
return scalar mu2 = r(mean)
return scalar sd2 = r(sd)
quietly sum `y3'
return scalar mu3 = r(mean)
return scalar sd3 = r(sd)
quietly sum `y4'
return scalar mu4 = r(mean)
return scalar sd4 = r(sd)
quietly sum `y5'
return scalar mu5 = r(mean)
return scalar sd5 = r(sd)
*
* end the program definition
*
end
*
* Set out seed
*
set seed 392481
*
* run simulation for 10 observations
*
simulate mu1 = r(mu1) mu2 = r(mu2) mu3 = r(mu3) mu4 = r(mu4) mu5=r(mu5) sd1 = r(sd1) sd2 = r(sd2) sd3 = r(sd3) sd4 = r(sd4) sd5 = r(sd5), ///
reps(10000) nodots: clt 10
*
* save this data
*
save clt10, replace
*
*  run simulation for 20 observations
*
simulate mu1 = r(mu1) mu2 = r(mu2) mu3 = r(mu3) mu4 = r(mu4) mu5=r(mu5) sd1 = r(sd1) sd2 = r(sd2) sd3 = r(sd3) sd4 = r(sd4) sd5 = r(sd5), ///
reps(10000) nodots: clt 20
*
* save this data
*
save clt20, replace
*
*  run simulation for 30 observations
*
simulate mu1 = r(mu1) mu2 = r(mu2) mu3 = r(mu3) mu4 = r(mu4) mu5=r(mu5) sd1 = r(sd1) sd2 = r(sd2) sd3 = r(sd3) sd4 = r(sd4) sd5 = r(sd5), ///
reps(10000) nodots: clt 30
*
* save this data
*
save clt30, replace
*
*  run simulation for 50 observations
*
simulate mu1 = r(mu1) mu2 = r(mu2) mu3 = r(mu3) mu4 = r(mu4) mu5=r(mu5) sd1 = r(sd1) sd2 = r(sd2) sd3 = r(sd3) sd4 = r(sd4) sd5 = r(sd5), ///
reps(10000) nodots: clt 50
*
* save this data
*
save clt50, replace
*
*  run simulation for 200 observations
*
simulate mu1 = r(mu1) mu2 = r(mu2) mu3 = r(mu3) mu4 = r(mu4) mu5=r(mu5) sd1 = r(sd1) sd2 = r(sd2) sd3 = r(sd3) sd4 = r(sd4) sd5 = r(sd5), ///
reps(10000) nodots: clt 200
*
* save this data
*
save clt200, replace
*
*  run simulation for 500 observations
*
simulate mu1 = r(mu1) mu2 = r(mu2) mu3 = r(mu3) mu4 = r(mu4) mu5=r(mu5) sd1 = r(sd1) sd2 = r(sd2) sd3 = r(sd3) sd4 = r(sd4) sd5 = r(sd5), ///
reps(10000) nodots: clt 500
*
* save this data
*
save clt500, replace
*
*  run simulation for 2000 observations
*
simulate mu1 = r(mu1) mu2 = r(mu2) mu3 = r(mu3) mu4 = r(mu4) mu5=r(mu5) sd1 = r(sd1) sd2 = r(sd2) sd3 = r(sd3) sd4 = r(sd4) sd5 = r(sd5), ///
reps(10000) nodots: clt 2000
*
* save this data
*
save clt2000, replace
*
*  run simulation for 4000 observations
*
simulate mu1 = r(mu1) mu2 = r(mu2) mu3 = r(mu3) mu4 = r(mu4) mu5=r(mu5) sd1 = r(sd1) sd2 = r(sd2) sd3 = r(sd3) sd4 = r(sd4) sd5 = r(sd5), ///
reps(10000) nodots: clt 4000
*
* save this data
*
save clt4000, replace
*
*  run simulation for 10000 observations
*
simulate mu1 = r(mu1) mu2 = r(mu2) mu3 = r(mu3) mu4 = r(mu4) mu5=r(mu5) sd1 = r(sd1) sd2 = r(sd2) sd3 = r(sd3) sd4 = r(sd4) sd5 = r(sd5), ///
reps(10000) nodots: clt 10000
*
* save this data
*
save clt10000, replace
*
*
* close log file
*
log close

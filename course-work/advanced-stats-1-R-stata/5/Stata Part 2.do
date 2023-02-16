*
*This program is takes data from simCLT and converts measures to z scores and then
* test the tail behavior (left and right)
* 
* Written by Dan Black on 11-1-2018
*
*
clear
capture log close
log using anSimTest.log, replace
*
* Sample using 10 observations
*
use clt10
gen z1 = (mu1-0.89)      /(sd1/10^(1/2))
gen z2 = (mu2-10)        /(sd2/10^(1/2))
gen z3 = (mu3-exp(1+1/2))/(sd3/10^(1/2))
gen z4 = (mu4-10)        /(sd4/10^(1/2))
gen z5 = mu5             /(sd5/10^(1/2))
*
* construct rejection level 5 percent rate; left and right tails
*
gen rrej1 = z1 >  1.96 & z1 < .
gen lrej1 = z1 < -1.96
gen rrej2 = z2 >  1.96 
gen lrej2 = z2 < -1.96
gen rrej3 = z3 >  1.96 
gen lrej3 = z3 < -1.96
gen rrej4 = z4 >  1.96 
gen lrej4 = z4 < -1.96
gen rrej5 = z5 >  1.96 
gen lrej5 = z5 < -1.96
*
* Should be 0.05, 1 binary 2 exponential 3 log-normal 4 Laplace 5 U-shaped
*

sum rrej1-lrej5 // 10 observations
/*
99% (-1%)  2.33
95% (-5%)  1.65
90% (-10%) 1.29
75% (-25%) 0.58
*/
* sum z1-z5, d // 10 observations
bitest lrej1 = 0.025 
bitest rrej1 = 0.025
bitest lrej2 = 0.025
bitest rrej2 = 0.025
bitest lrej3 = 0.025
bitest rrej3 = 0.025
bitest lrej4 = 0.025
bitest rrej4 = 0.025
bitest lrej5 = 0.025
bitest rrej5 = 0.025
clear
*
* Sample using 20 observation
*
use clt20
gen z1 = (mu1-0.89)      /(sd1/20^(1/2))
gen z2 = (mu2-10)        /(sd2/20^(1/2))
gen z3 = (mu3-exp(1+1/2))/(sd3/20^(1/2))
gen z4 = (mu4-10)        /(sd4/20^(1/2))
gen z5 = mu5             /(sd5/20^(1/2))
*
* construct rejection level  5 percent rate; left and right tails
*
gen rrej1 = z1 >  1.96 & z1 < .
gen lrej1 = z1 < -1.96
gen rrej2 = z2 >  1.96 
gen lrej2 = z2 < -1.96
gen rrej3 = z3 >  1.96 
gen lrej3 = z3 < -1.96
gen rrej4 = z4 >  1.96 
gen lrej4 = z4 < -1.96
gen rrej5 = z5 >  1.96 
gen lrej5 = z5 < -1.96
*
* Should be 0.05, 1 binary 2 exponential 3 log-normal 4 Laplace 5 U-shaped
*

sum rrej1-lrej5 // 20 observations
/*
99% (-1%)  2.33
95% (-5%)  1.65
90% (-10%) 1.29
75% (-25%) 0.58
*/
* sum z1-z5, d // 20 observations
bitest lrej1 = 0.025 
bitest rrej1 = 0.025
bitest lrej2 = 0.025
bitest rrej2 = 0.025
bitest lrej3 = 0.025
bitest rrej3 = 0.025
bitest lrej4 = 0.025
bitest rrej4 = 0.025
bitest lrej5 = 0.025
bitest rrej5 = 0.025
clear
*
* Sample using 30 observation 
*
use clt30
gen z1 = (mu1-0.89)      /(sd1/30^(1/2))
gen z2 = (mu2-10)        /(sd2/30^(1/2))
gen z3 = (mu3-exp(1+1/2))/(sd3/30^(1/2))
gen z4 = (mu4-10)        /(sd4/30^(1/2))
gen z5 = mu5             /(sd5/30^(1/2))
*
* construct rejection level  5 percent rate; left and right tails
*
gen rrej1 = z1 >  1.96 & z1 < .
gen lrej1 = z1 < -1.96
gen rrej2 = z2 >  1.96 
gen lrej2 = z2 < -1.96
gen rrej3 = z3 >  1.96 
gen lrej3 = z3 < -1.96
gen rrej4 = z4 >  1.96 
gen lrej4 = z4 < -1.96
gen rrej5 = z5 >  1.96 
gen lrej5 = z5 < -1.96
*
* Should be 0.05, 1 binary 2 exponential 3 log-normal 4 Laplace 5 U-shaped
*
sum rrej1-lrej5 // 30 observations
/*
99% (-1%)  2.33
95% (-5%)  1.65
90% (-10%) 1.29
75% (-25%) 0.58
*/
* sum z1-z5, d  // 30 observations
bitest lrej1 = 0.025
bitest rrej1 = 0.025
bitest lrej2 = 0.025
bitest rrej2 = 0.025
bitest lrej3 = 0.025
bitest rrej3 = 0.025
bitest lrej4 = 0.025
bitest rrej4 = 0.025
bitest lrej5 = 0.025
bitest rrej5 = 0.025
clear

* Sample using 50 observation
*
use clt50
gen z1 = (mu1-0.89)      /(sd1/50^(1/2))
gen z2 = (mu2-10)        /(sd2/50^(1/2))
gen z3 = (mu3-exp(1+1/2))/(sd3/50^(1/2))
gen z4 = (mu4-10)        /(sd4/50^(1/2))
gen z5 = mu5             /(sd5/50^(1/2))
*
* construct rejection level  5 percent rate; left and right tails
*
gen rrej1 = z1 >  1.96 
gen lrej1 = z1 < -1.96
gen rrej2 = z2 >  1.96 
gen lrej2 = z2 < -1.96
gen rrej3 = z3 >  1.96 
gen lrej3 = z3 < -1.96
gen rrej4 = z4 >  1.96 
gen lrej4 = z4 < -1.96
gen rrej5 = z5 >  1.96 
gen lrej5 = z5 < -1.96
*
* Should be 0.05, 1 binary 2 exponential 3 log-normal 4 Laplace 5 U-shaped
*
sum rrej1-lrej5 // 50 observations
/*
99% (-1%)  2.33
95% (-5%)  1.65
90% (-10%) 1.29
75% (-25%) 0.58
*/
* sum z1-z5, d  // 50 observations
bitest lrej1 = 0.025
bitest rrej1 = 0.025
bitest lrej2 = 0.025
bitest rrej2 = 0.025
bitest lrej3 = 0.025
bitest rrej3 = 0.025
bitest lrej4 = 0.025
bitest rrej4 = 0.025
bitest lrej5 = 0.025
bitest rrej5 = 0.025
clear
*
* Sample using 200 observation
*
use clt200
gen z1 = (mu1-0.89)      /(sd1/200^(1/2))
gen z2 = (mu2-10)        /(sd2/200^(1/2))
gen z3 = (mu3-exp(1+1/2))/(sd3/200^(1/2))
gen z4 = (mu4-10)        /(sd4/200^(1/2))
gen z5 = mu5             /(sd5/200^(1/2))
*
* construct rejection level  5 percent rate; left and right tails
*
gen rrej1 = z1 >  1.96 
gen lrej1 = z1 < -1.96
gen rrej2 = z2 >  1.96 
gen lrej2 = z2 < -1.96
gen rrej3 = z3 >  1.96 
gen lrej3 = z3 < -1.96
gen rrej4 = z4 >  1.96 
gen lrej4 = z4 < -1.96
gen rrej5 = z5 >  1.96 
gen lrej5 = z5 < -1.96
*
* Should be 0.05, 1 binary 2 exponential 3 log-normal 4 Laplace 5 U-shaped
*
sum rrej1-lrej5  // 200 observations
/*
99% (-1%)  2.33
95% (-5%)  1.65
90% (-10%) 1.29
75% (-25%) 0.58
*/
* sum z1-z5, d  // 200 observations
bitest lrej1 = 0.025
bitest rrej1 = 0.025
bitest lrej2 = 0.025
bitest rrej2 = 0.025
bitest lrej3 = 0.025
bitest rrej3 = 0.025
bitest lrej4 = 0.025
bitest rrej4 = 0.025
bitest lrej5 = 0.025
bitest rrej5 = 0.025
clear
*
* Sample using 500 observation
*
use clt500
gen z1 = (mu1-0.89)      /(sd1/500^(1/2))
gen z2 = (mu2-10)        /(sd2/500^(1/2))
gen z3 = (mu3-exp(1+1/2))/(sd3/500^(1/2))
gen z4 = (mu4-10)        /(sd4/500^(1/2))
gen z5 = mu5             /(sd5/500^(1/2))
*
* construct rejection level  5 percent rate; left and right tails
*
gen rrej1 = z1 >  1.96 
gen lrej1 = z1 < -1.96
gen rrej2 = z2 >  1.96 
gen lrej2 = z2 < -1.96
gen rrej3 = z3 >  1.96 
gen lrej3 = z3 < -1.96
gen rrej4 = z4 >  1.96 
gen lrej4 = z4 < -1.96
gen rrej5 = z5 >  1.96 
gen lrej5 = z5 < -1.96
*
* Should be 0.05, 1 binary 2 exponential 3 log-normal 4 Laplace 5 U-shaped
*
sum rrej1-lrej5  // 500 observations
/*
99% (-1%)  2.33
95% (-5%)  1.65
90% (-10%) 1.29
75% (-25%) 0.58
*/
* sum z1-z5, d  // 500 observations
bitest lrej1 = 0.025
bitest rrej1 = 0.025
bitest lrej2 = 0.025
bitest rrej2 = 0.025
bitest lrej3 = 0.025
bitest rrej3 = 0.025
bitest lrej4 = 0.025
bitest rrej4 = 0.025
bitest lrej5 = 0.025
bitest rrej5 = 0.025
clear
*
* Sample using 2000 observation  5 percent rate
*
use clt2000
gen z1 = (mu1-0.89)      /(sd1/2000^(1/2))
gen z2 = (mu2-10)        /(sd2/2000^(1/2))
gen z3 = (mu3-exp(1+1/2))/(sd3/2000^(1/2))
gen z4 = (mu4-10)        /(sd4/2000^(1/2))
gen z5 = mu5             /(sd5/2000^(1/2))
*
* construct rejection level; left and right tails
*
gen rrej1 = z1 >  1.96 
gen lrej1 = z1 < -1.96
gen rrej2 = z2 >  1.96 
gen lrej2 = z2 < -1.96
gen rrej3 = z3 >  1.96 
gen lrej3 = z3 < -1.96
gen rrej4 = z4 >  1.96 
gen lrej4 = z4 < -1.96
gen rrej5 = z5 >  1.96 
gen lrej5 = z5 < -1.96
*
* Should be 0.05, 1 binary 2 exponential 3 log-normal 4 Laplace 5 U-shaped
*
sum rrej1-lrej5 // 2000 observations
/*
99% (-1%)  2.33
95% (-5%)  1.65
90% (-10%) 1.29
75% (-25%) 0.58
*/
*sum z1-z5, d  // 2000 observations
bitest lrej1 = 0.025
bitest rrej1 = 0.025
bitest lrej2 = 0.025
bitest rrej2 = 0.025
bitest lrej3 = 0.025
bitest rrej3 = 0.025
bitest lrej4 = 0.025
bitest rrej4 = 0.025
bitest lrej5 = 0.025
bitest rrej5 = 0.025
clear
*
* Sample using 4000 observation  5 percent rate
*
use clt4000
gen z1 = (mu1-0.89)      /(sd1/4000^(1/2))
gen z2 = (mu2-10)        /(sd2/4000^(1/2))
gen z3 = (mu3-exp(1+1/2))/(sd3/4000^(1/2))
gen z4 = (mu4-10)        /(sd4/4000^(1/2))
gen z5 = mu5             /(sd5/4000^(1/2))
*
* construct rejection level
*
gen rrej1 = z1 >  1.96 
gen lrej1 = z1 < -1.96
gen rrej2 = z2 >  1.96 
gen lrej2 = z2 < -1.96
gen rrej3 = z3 >  1.96 
gen lrej3 = z3 < -1.96
gen rrej4 = z4 >  1.96 
gen lrej4 = z4 < -1.96
gen rrej5 = z5 >  1.96 
gen lrej5 = z5 < -1.96
*
* Should be 0.05, 1 binary 2 exponential 3 log-normal 4 Laplace 5 U-shaped
*
sum rrej1-lrej5 // 4000 observations
/*
99% (-1%)  2.33
95% (-5%)  1.65
90% (-10%) 1.29
75% (-25%) 0.58
*/
*sum z1-z5, d  // 4000 observations
bitest lrej1 = 0.025
bitest rrej1 = 0.025
bitest lrej2 = 0.025
bitest rrej2 = 0.025
bitest lrej3 = 0.025
bitest rrej3 = 0.025
bitest lrej4 = 0.025
bitest rrej4 = 0.025
bitest lrej5 = 0.025
bitest rrej5 = 0.025
clear
*
* Sample using 4000 observation  5 percent rate; left and right tails
*
use clt10000
gen z1 = (mu1-0.89)      /(sd1/10000^(1/2))
gen z2 = (mu2-10)        /(sd2/10000^(1/2))
gen z3 = (mu3-exp(1+1/2))/(sd3/10000^(1/2))
gen z4 = (mu4-10)        /(sd4/10000^(1/2))
gen z5 = mu5             /(sd5/10000^(1/2))
*
* construct rejection level
*
gen rrej1 = z1 >  1.96 
gen lrej1 = z1 < -1.96
gen rrej2 = z2 >  1.96 
gen lrej2 = z2 < -1.96
gen rrej3 = z3 >  1.96 
gen lrej3 = z3 < -1.96
gen rrej4 = z4 >  1.96 
gen lrej4 = z4 < -1.96
gen rrej5 = z5 >  1.96 
gen lrej5 = z5 < -1.96
*
* Should be 0.05, 1 binary 2 exponential 3 log-normal 4 Laplace 5 U-shaped
*
sum rrej1-lrej5 // 10000 observations
/*
99% (-1%)  2.33
95% (-5%)  1.65
90% (-10%) 1.29
75% (-25%) 0.58
*/
*sum z1-z5, d  // 10000 observations
bitest lrej1 = 0.025
bitest rrej1 = 0.025
bitest lrej2 = 0.025
bitest rrej2 = 0.025
bitest lrej3 = 0.025
bitest rrej3 = 0.025
bitest lrej4 = 0.025
bitest rrej4 = 0.025
bitest lrej5 = 0.025
bitest rrej5 = 0.025
*
*
*
*
* close log file
*
log close

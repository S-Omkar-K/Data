clear 

capture log close 

set more off

log using Sai_Omkar_Kandukuri_PS3.log, replace

set obs 50

generate p1 = runiform()

generate x = 1 if p1 <= 0.3
generate y = 1 if p1 <= 0.25

replace x = 2 if p1 > 0.3 & p1 <= 0.7 
replace x = 3 if p1 > 0.7 & p1 <= 1


replace y = 2 if p1 > 0.25 & p1 <= 0.4
replace y = 3 if p1 >0.4 & p1 <= 0.6
replace y = 4 if p1 > 0.6 & p1 <= 1

sum x, detail
sum y, detail

tabulate x y

correlate x y, covariance

pwcorr x y





clear 

set more off



set seed 18112021

set obs 500

generate p1 = runiform()

generate x = 1 if p1 <= 0.3
replace x = 2 if p1 > 0.3 & p1 <= 0.7 
replace x = 3 if p1 > 0.7 & p1 <= 1

generate y = 1 if p1 <= 0.25
replace y = 2 if p1 > 0.25 & p1 <= 0.4
replace y = 3 if p1 >0.4 & p1 <= 0.6
replace y = 4 if p1 > 0.6 & p1 <= 1

sum x, detail
sum y, detail


tabulate x y

correlate x y, covariance

pwcorr x y





clear 

set more off



set seed 18112021

set obs 10000

generate p1 = runiform()

generate y = 1 if p1 <= 0.25
generate x = 1 if p1 <= 0.3
replace y = 2 if p1 > 0.25 & p1 <= 0.4
replace y = 3 if p1 >0.4 & p1 <= 0.6
replace x = 2 if p1 > 0.3 & p1 <= 0.7 
replace y = 4 if p1 > 0.6 & p1 <= 1
replace x = 3 if p1 > 0.7 & p1 <= 1





sum x, detail
sum y, detail


tabulate x y

correlate x y, covariance

pwcorr x y


log close

translate Sai_Omkar_Kandukuri_PS3.log Sai_Omkar_Kandukuri_PS3.pdf
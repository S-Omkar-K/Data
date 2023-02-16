
clear 
capture log close
set more off
log using Stata_Sai_Omkar_K_PS8.log, replace

use "C:\Users\saiomkark\OneDrive - The University of Chicago\AdvStats\PS8\homework_8.dta"

summarize

*1. Using the experimental data, test whether the those treated are more likely to work in the year after treatment.
*A Use the t-test command;

ttest work, by(treated) unequal level(95) welch

*Observed p-value for the t-test with a 95% confidence interval is 0.0185. This value is less than 0.05. So, the Null hypothesis can be rejected and Alternative Hypothesis(that the true difference in means of work in the year between treated and not treated people is not equal to 0) cannot be rejected. 

*B Use the chi-square test;
tabi 230 67 \ 296 129, chi2

*Observed p-value here is 0.020 for this test. As the observed p-value is less than 0.05, we can reject the Null Hypothesis. And we cannot reject the alternate hypothesis that probability of working in the year is same for treated and not treated is not equal.

*C Use Fisher’s exact test;
cci 230 67 296 129, exact

*Observed p-value is 0.0218 for the two-tail fisher exact test. As this p-value is less than 0.05, we can reject the Null hypothesis that the probability of work is same for both treated and not treated is equal to 1 i.w true odds ratio is equal to 1. Also, we cannot reject the Alternate Hypothesis that the probability of work between people with treatment and no treatement is not same i.e true odds ratio is not equal to 1. 

*D Why do the p-values on the two-sided test differ? Which should you believe?

*We observed the following p values 
* t-test : 0.0185 , Chi-square test : 0.02, Fisher exact test : 0.0218
* As we compare the different tests, Fisher exact test is preferred as its an asymptotic test and fits for the binary data such as to compare the treated/non treated data. Fisher test also provides an accurate significance level without relying on the assumptions where as asymptotic tests make assumptions about the data. When we have extremely large sample size, then it is infeasable to perform Fisher test. In such situations, we can prefer Chi-square test as the accuracy increases as the sample size increases. 





*2. Using the regression command, test whether the those treated are more likely to work in the year after treatment.

*A Regress work against the treatment indicator and test the hypothesis;

regress work treated

*Observed p-value = 0.0205 with a 95% confidence interval is less than 0.05. So, we can reject the null hypothesis and not the Alternate hypothesis that the true difference in means of work in year between treated and not treated is not equal to 0.

*B Regress work against the treatment indicator and all other covariates in the data set.

regress work treated age educ black married hisp

* What happens to the R2of the regression equation? 

*We observed a higher adjusted R square value. This means that the additional input variables are adding value to the model. In univariate regression model , we observed a adjused R square value of 0.0061 where are the adjusted R square value is 0.0300 with the muti variate regressin model. This means a better fit of the model. 

*What happens to the treatment indicator? Explain why you see these results. Compare them to the results in Problem 1.

*Univariate model 

*        work |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
*-------------+----------------------------------------------------------------
*     treated |   .0779402   .0335553     2.32   0.020     .0120623    .1438181


*Multivariate model


*        work |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
*-------------+----------------------------------------------------------------
*     treated |   .0775439   .0332208     2.33   0.020     .0123219    .1427658

*As seen above, the treatment indicator Coeff/estimate decreases slightly, but however it can still be considered that the treatment indicator still has majority of influence on the work.  This slight decrease may be because of the introducing other variables into the equation. This is same in the case of Standard error and residual standard error where both decrease due to the introduction of other variables into the regression model. 

* p-value t-test : 0.0185 , Chi-square test : 0.02, Fisher exact test : 0.0218
* p-value for univariate model : 0.0205 and 0.0001 for multivariate. Comparing the p-values , regression is a better alternative model to the models used in the question 1. 


*3. Given the data from the experiment, do the following:
*A Derive the marginal pmf of work when treated;
*B Derive the marginal pmf of work when not treated;
tab treated work, row


*C Derive the Frechet-Hoeffding bounds for the joint distribution.

* People who benefots from treatment : Bounds of joint distribution are [0.07, 0.30]
* People who loses from the treatment : Bounds of joint distribution are [0.00, 0.23]


*4 4. Consider the following mythical experiment. There are two treatment arms: vaccination with the Moderna vaccine (n = 14, 598) and vaccination with the Pfizer vaccine (n = 21, 669). Suppose 100 of those with the Pfizer vaccine develop Covid and 269 of those with Moderna vaccine have Covid.
*A Test the hypothesis that the vaccines are equally effective against the alternative that they are not.

*From above information 
*             Not affected       Affected
*Moderna       14329              269
*Pfizer        21569              100


*Fisher exact test
cci 14329 269 21569 100, exact

*Observed p-value 0 for two-tail fisher exact test is less than 0.05. So we can reject the null hypothesis that vaccines are equally effective (or) i.e true odds ratio is equal to 1)=. Also we cannot reject the alternate hypothesis that the vaccines are not equally effective (or) efficacy is not same for both i.e true odds ratio is not equal to 1.


* B These are the actually numbers from the treated observations of the Moderna and Pfizer clinical trials. Explain why this is not a legitimate experimental trial.

*Two arguments here. One is we donot have data of a person in two cases where in one case a vaccine is administered and other case where the vaccine is not administered. In case, we have both the data of a person, we can effectively compare the results in both the cases i.e vaccinated state and unvaccinated state. As we donot have the complete data, we cannot construct a counterfactual which deems these experimental trials cannot be considered legitimate. Thus, the comparision of efficacies of two vaccines cannot be considered legit.

*Another argument is, because we do not have a treatment and control group. If we were to have data of both the treatment and control group, then we can treat this experiment triel as legitimate. Thus the insights we got from comparison of efficacies of the two vaccines based on only the treatment group data is not legitimate.






log close

translate Stata_Sai_Omkar_K_PS8.log Stata_Sai_Omkar_K_PS8.pdf
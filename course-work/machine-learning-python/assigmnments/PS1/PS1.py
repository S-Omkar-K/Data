# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 11:04:16 2023

@author: saiom
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels.formula.api as smf
import statsmodels.api as sm


#### Question 1C   ####


# To begin, load in the Boston data set.

boston_data = pd.read_csv("E:\Winter'23\ML\PS1\Boston\Boston.csv")

# How many rows are in this data set? How many columns?
# What do the rows and columns represent?
np.shape(boston_data)

# Number of Rows= 506
# Number of Columnns = 14
# Rows and columns description:
#    Each row is a tract of land.
#    Each column is a feature that affect the


# Make some pairwise scatterplots of the predictors (columns) in this data set.
# Describe your findings

sns.pairplot(boston_data[['INDUS', 'ZN', 'DIS']])

#  Now lets examine few pairs and see the relations,

#  Examining relation between LSTAT and MDEV

plt.scatter(boston_data['LSTAT'], boston_data['MDEV'])
plt.xlabel('% lower status of the population')
plt.ylabel('Median value of owner-occupied homes in $1000s')

#   It looks like that there is a negative correlation
#   between LSTAT and MDEV since LSTAT is the percentage of lower status people,
#   who usually have lower incomes and thus own cheaper houses.


#   Examining relation between RM and MDEV

plt.scatter(boston_data['RM'], boston_data['MDEV'])
plt.xlabel('Average number of rooms per dwelling')
plt.ylabel('Median value of owner-occupied homes in $1000s')

#   It appears that there is a positive correlation
#   between RM(Av. number of rooms) and the MDEV(Median valye of home),
#   which is as expected. Since more space typically leads to a higher price.


# Are any of the predictors associated with per capita crime rate?
# If so, explain the relationship.

boston_data.corrwith(boston_data['CRIM'])

# CRIM       1.000000
#ZN        -0.199458
# INDUS      0.404471
#CHAS      -0.055295
# NOX        0.417521
#RM        -0.219940
# AGE        0.350784
#DIS       -0.377904
# RAD        0.622029
# TAX        0.579564
# PTRATIO    0.288250
#B         -0.377365
# LSTAT      0.452220
#MDEV      -0.385832

# We can also analyze the relation by plotting pairplots

sns.pairplot(boston_data, x_vars=[
             "RAD", "LSTAT", "MDEV", "DIS"], y_vars=["CRIM"])

# From the plots, we can observe that there is clear relationship between the variables
# and per capita crime rate. From the plots we can say that tracts with lower
# home values have higher crime rate. Similarly tracts near to the Employment
# centers also have higher per capita crime rate.

# The predictor with highest correlation with CRIM is RAD(index of
# accessibility to radial highways)

# Futher analysis the relationship between RAD-CRIM and TAX-CRIM

sns.boxplot(boston_data['RAD'], boston_data['CRIM'])

# The boxplot shows that the when the value of RAD is 24, the average percapita
# crime rate by town is higher and the range is also large compared to when the
# RAD is lower.


# Do any of the census tracts of Boston appear to have particularly
# high crime rates? Tax rates? Pupil-teacher ratios? Comment on
# the range of each predictor


boston_data['CRIM'].nlargest(5)
# We observe that a particular tract id 380 has the highest rate at 88.9762
# The next ones are 418 73.5341, 405 67.9208, 410  1.1358, 414 45.7461
boston_data['CRIM'].describe()
# The minimum crime rate is 0.006320, the maximum is 88.97620,
# the mean and median are 3.593761, 0.256510. Range is 88.97


boston_data['TAX'].nlargest(10)
# The largest group contains 5 tracts(488, 489, 490, 491, 492) of tax rates
# is at $711.0 and the next largest is at $666.0 for
boston_data['TAX'].describe()
# The minimum tax rate is $187 per $10000, the maximum is $711.0,
# the mean and median are $408.24, $330. Range is $524


boston_data['PTRATIO'].nlargest(10)
# The largest group contains two tracts(354, 355) with 22.0 ratio and
# the next group contain 15 trackts with a ratio of 21.2
boston_data['PTRATIO'].describe()
# The minimum pupil teacher ratio is 12.60 pupils per teacher,
# the maximum is 22 pupils per teacher
# the mean and median are 18.45, 19.05. Range is 9.4


# How many of the census tracts in this data set bound the Charles river?

# CHAS Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)

boston_data["CHAS"].sum()

# 35 census tracts in this data set bound the Charles River.


# What is the median pupil-teacher ratio among the towns in this data set?

boston_data["PTRATIO"].median()

# The median pupil-teacher ration in this data set is 19.05


# Which census tract of Boston has lowest median value of owner occupied homes?
# What are the values of the other predictors for that census tract,
# and how do those values compare to the overall ranges for those predictors?

boston_data[boston_data['MDEV'] == boston_data['MDEV'].min()]

# The census tract with id 398 and 405 have lowest median value of owner
# occupied homes value at 5.0 (in 1000s).

boston_data.iloc[398]

# CRIM        38.3518
# ZN           0.0000
# INDUS       18.1000
# CHAS         0.0000
# NOX          0.6930
# RM           5.4530
# AGE        100.0000
# DIS          1.4896
# RAD         24.0000
# TAX        666.0000
# PTRATIO     20.2000
# B          396.9000
# LSTAT       30.5900
# MDEV         5.0000

boston_data.iloc[405]

# CRIM        67.9208
# ZN           0.0000
# INDUS       18.1000
# CHAS         0.0000
# NOX          0.6930
# RM           5.6830
# AGE        100.0000
# DIS          1.4254
# RAD         24.0000
# TAX        666.0000
# PTRATIO     20.2000
# B          384.9700
# LSTAT       22.9800
# MDEV         5.0000


boston_data.describe()

# The tract with id 398 has a large CRIM compared to mean, ZN below quantile 75%,
# greater than the mean INDUS 11.13, do not bound the Charles river,
# greater than the mean NOX 0.55, RM below the 25% quantile,
# AGE 100, DIS just greater than the minimum value 1.126,
# maximum RAD, TAX in 75% quantile, B is at maximum and
# LSTAT above 75% quantile, and MDEV at the minimum at 5.0.
# All units are as per prescribed.


# The tract with id 405 has a higher CRIM compared to mean CRIM, ZN of 0,
# greater than the mean INDUS, do not bound the Charles river,
# greater than the mean NOX 0.55, RM below the 25% quantile,
# AGE 100, DIS just greater than the minimum value 1.126,
# RAD maximum of 24, TAX in 75% quantile, B is at maximum and
# LSTAT above 75% quantile, and MDEV at the minimum at 5.0.
# All units are as per prescribed.


# In this data set, how many of the census tracts average more
# than seven rooms per dwelling? More than eight rooms per
# dwelling? Comment on the census tracts that average more than
# eight rooms per dwelling

len(boston_data[boston_data['RM'] > 7])
# 64 census tracts average more than 7 rooms per dwelling.

len(boston_data[boston_data['RM'] > 8])
# 13 census tracts average more than 8 rooms per dwelling

boston_data[boston_data['RM'] > 8].describe().round()

# For the census tracts that average more than eight rooms per dwelling, it
# has a lower mean CRIM of 1.0 compared to the mean CRIM of 3.53, a lower
# mean INDUS proportion at 7 compared to the overall mean INDUS of 11.14,
# higher proporation of Black population at 385.0 compared to the overall mean
# of 356.61, very high median value of 44 compared to overall mean of 23.


# Part a
coefficients1 = {}
predictors = [k for k in list(boston_data) if k not in ["CRIM"]]

plt.figure(figsize=(20, 20))
for k, predictor in enumerate(predictors):
    reg = 'CRIM ~ ' + predictor
    y = smf.ols(formula=reg, data=boston_data).fit()
    coefficients1[predictor] = [y.params[predictor]]
    print(predictor + ':' +
          ' COEFF : ' + str(y.params[predictor]) +
          ' p-value : ' + str(y.pvalues[predictor]))
    plt.subplot(5, 3, k + 1)
    plt.xlabel(predictor)
    plt.ylabel("CRIM")
    plt.scatter(boston_data[predictor], boston_data['CRIM'])
    plt.plot(boston_data[predictor], y.fittedvalues)


# From the above results we can observe that, there is enough statistcal
# evidence that predictors are associated to CRIM i.e the response,
# except for one predictor CHAS.


# Part b
predictors2 = "+".join([c for c in predictors if c not in ["CRIM"]])
reg_2 = 'CRIM ~ ' + predictors2
y2 = smf.ols(reg_2, boston_data).fit()
y2.summary()

# The results show an R-square of 0.448, F-statistic of 30.73 and coefficients
# as shown above. Observing p-values and t-statistics, we can reject the null
# hypothesis for every predictor except for DIS and RAD at 1% elevel.


# Part c

# Compared to part 1, we observed that more predictors are deemed
# to be insignificant in our analysis in predicting in part c.

for predictor in coefficients1:
    coefficients1[predictor].append(y2.params[predictor])


x = [coefficients1[predictor][0] for predictor in coefficients1]
y = [coefficients1[predictor][1] for predictor in coefficients1]


plt.scatter(x, y)
plt.xlabel('univariate regression coefficients from (a)')
plt.ylabel('multiple regression coefficients from (b)')


# Part d


plt.figure(figsize=(20, 20))
for k, predictor in enumerate(predictors):
    reg_3 = 'CRIM ~ ' + predictor + \
        "+ np.power(" + predictor + ", 2) + np.power(" + predictor + ", 3)"
    y3 = smf.ols(formula=reg_3, data=boston_data).fit()
    plt.subplot(4, 4, k + 1)
    plt.xlabel(predictor)
    plt.ylabel("CRIM")
    plt.scatter(boston_data[predictor], boston_data['CRIM'])
    plt.plot(boston_data[predictor], y3.fittedvalues)
    x = np.linspace(min(boston_data[predictor]), max(boston_data[predictor]))
    y = y3.params[0] + x*y3.params[1] + \
        (x**2)*y3.params[2] + (x**3)*y3.params[3]
    plt.plot(x, y)
    print('Predictor : ' + predictor)
    print(y3.summary())


# ANalysis of TAX non linear regression summary:
# ====================================================================================
#                       coef    std err          t      P>|t|      [0.025      0.975]
# ------------------------------------------------------------------------------------
# Intercept           19.0705     11.827      1.612      0.107      -4.166      42.307
# TAX                 -0.1524      0.096     -1.589      0.113      -0.341       0.036
# np.power(TAX, 2)     0.0004      0.000      1.476      0.141      -0.000       0.001
# np.power(TAX, 3) -2.193e-07   1.89e-07     -1.158      0.247   -5.91e-07    1.53e-07

# The p-value for B2 i.e squared relationship is 0.141. Therefore we cannot reject
# the null hypothesis that B2 = 0. The p-value for B3 i.e cubic relationship is 0.247.
# There fore again we cannot reject the null hypothesis that B3 = 0. This concludes that
# we cannot for certain say that there is a non linear relationship between TAX and CRIM.


# From the summaries of all the regressions, we can observe enough strong evidence for
# a non linear association, between the predictors INDUS, AGE, NOX, DIS, PTRATIO
# MDEV with the response. The other predictors can be categorized similarly into
# some evidence for the non linear relationship with response and categorized into no evidence(RAD,RM, TAX, B, LSTAT) of a linear relationship with response.

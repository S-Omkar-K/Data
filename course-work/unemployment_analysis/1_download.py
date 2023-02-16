"""
Data and Programming 2 
Final Project - Aditya Anmol, Jahnvi Agarwal, Sai Omkar
"""
import pandas as pd 
from pandas_datareader import wb
import requests
import os

work_dir = '/Users/adityaanmol/Documents/GitHub/Unemployment_Analysis'
file = '/data_inputs'
os.chdir(work_dir)

def get_wb_dta(indicators, countries, start, end):
    wb_main = pd.DataFrame()
    for indicator in indicators:
        dta =  wb.download(indicator=indicator, country=countries, start=start, end=end)
        wb_main = merge_dta(wb_main, dta)
    return wb_main 

def merge_dta(wb_main,dta):
    if wb_main.empty:
        wb_main = dta
    else:
        wb_main = wb_main.merge(dta,on=['country','year'],how='outer')
    return wb_main


indicators_wb = ['FP.CPI.TOTL.ZG','SL.UEM.TOTL.ZS']
#user imput in based in shiny
start = 1996
end = 2020


country_dta = pd.read_csv(os.path.join(work_dir+file,'oecd_country_iso.csv'))
country_2 = list(country_dta['Alpha-2 Code'])
country_3 = list(country_dta['Alpha-3 Code'])

wb_data = get_wb_dta(indicators_wb, country_2, start, end)
wb_col = {'FP.CPI.TOTL.ZG':'Inflation', 'SL.UEM.TOTL.ZS': 'Unemployment Rate'}
wb_data.rename(columns = wb_col, inplace = True) 


#OECD 

# Avg Wage, Exchange Rate, Old-Age Dependency, Pop with tertiary education,
# Public Spending on unemployment, Import, Export, Working Age Pop

def read_oecd(work_dir, file, csv_name, start, end, cntry_l):
    dta = pd.read_csv(os.path.join(work_dir+file,csv_name))
    edited = dta[['LOCATION','TIME','Value']]
    col_name = csv_name[:-4]
    edited.rename(columns = {'LOCATION':'country','TIME':'year','Value':col_name}, inplace =True)
    edited = edited.loc[(edited['year']>=start)&(edited['year']<=end)]#.between(start,end, inclusive=True)]
    edited = edited[edited.country.isin(cntry_l)]
    edited.reset_index(inplace=True)
    edited = edited[['country','year',col_name]]
    return edited

entries = os.listdir(work_dir+file)
entries = [item for item in entries if item != 'oecd_country_iso.csv']

oecd_main = pd.DataFrame()
for f_name in entries[1:]:
    oecd_dta = read_oecd(work_dir, file, f_name, start, end, country_3)
    oecd_main = merge_dta(oecd_main, oecd_dta)
    

# Match & Convert 3 digit code to 2 digit 

#merge
#max row 950 - wb
#oecd mx 925

output = wb_data
output.to_csv('/Users/adityaanmol/Documents/GitHub/Unemployment_Analysis/shiny_app/output_dta.csv')
    



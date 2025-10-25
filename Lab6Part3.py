# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 08:22:17 2025

@author: Kenya Dacoulis and Carlyn Matar
"""

#Part 3 

import pandas as pd

data = pd.read_csv('wdi_wide.csv')

#Part 3.3
info = data.info()

# number of empty values physicians: 217-207 = 10; empty values
# number of empty values populations: 217-217 = 0; no empty values

#Part 3.4
unique_values = data.nunique()
print(unique_values)

#Part 3.5
further_info = data.describe()
print(further_info)

# gives count, mean, standard deviation, minimum, max, 

#Part 3.6
data['GNI per capita'] = round(data['GNI']/ data['Population'])

# Part 3.7
country_count_per_region = pd.value_counts(data['Region'])

high_income_country_count = pd.value_counts(data['High Income Economy'])

# Part 3.8
high_income_location = pd.crosstab(data['High Income Economy'], data['Region'])
print(high_income_location)

# Part 3.9
filtered_data = data[data['Life expectancy, female'] > 80]

for i in filtered_data["Country Name"]:
    print(i)
    

#Part 4 
import seaborn as sns

#Part 4.1 and 4.2
sns.relplot(data, x='Life expectancy, female', y='GNI per capita', hue= 'Region')
sns.relplot(data, x='Life expectancy, male', y='GNI per capita', hue= 'Region')
#yes, we inverted the y and x axis to better show the curve, but essentially, as the GNI per capita increases, the life expectancy also increases. 

#Part 4.3
sns.relplot(data, x='Life expectancy, female', y='GNI per capita', hue='Region', kind='line', errorbar = 'sd')
sns.relplot(data, x='Life expectancy, male', y='GNI per capita', hue='Region', kind='line', errorbar = 'sd')
#The standard deviation doesn't show since it's always 0, as each colum represents the data from a single country, so theres only one trial

#Part 4.4
sns.lmplot(data, x= 'Life expectancy, female', y='GNI per capita', hue= 'Region')
sns.lmplot(data, x= 'Life expectancy, male', y='GNI per capita', hue= 'Region')
# These plots are similar to the ones above, with scatter plots, but with additional linear regressions over them for better visualization

#Part 4.5

#First question : Does tertiary education affect male and female life expectancies, and does it differ in each region?
sns.relplot(data, x='Life expectancy, female', y='Tertiary education, female', col= 'Region')
sns.relplot(data, x='Life expectancy, male', y='Tertiary education, male', col= 'Region')
    #Female life expectanciy, in relation to it's tertiary education, has similar results to the male expectancy in each region. 
    #The main differences occur between different regions, for example, in Asia and Africa, life expectancy depends alot more on 
    #their education (there's a clear correlation ), than in Europe or America (where the plots are more scattered)


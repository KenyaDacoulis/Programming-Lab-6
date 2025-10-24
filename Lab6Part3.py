# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 08:22:17 2025

@author: Kenya Dacoulis and Carlyn Matar
"""

import pandas as pd
import seaborn as sns

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

data['GNI per capita'] = data['GNI']/ data['Population']
pd.round(data['GNI per capita'])

# Part 3.7

country_count_per_region = pd.value_counts(data['Region'])

high_income_country_count = pd.value_counts(data['High Income Economy'])

# Part 3.8

high_income_location = pd.crosstab(data['High Income Economy'], data['Region'])
print(high_income_location)

# Part 3.9

country_count_female_over_80 = 0
for i in data['Life expenctancy, female']:
    if i > 80:
        country_count_female_over_80 += 1
        
    



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
#Yes, we inverted the y and x axis to better show the curve, but essentially, as the GNI per capita increases, the life expectancy also increases. 

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
    #Yes, female life expectanciy, in relation to it's tertiary education, has similar results to the male expectancy in each region. 
    #The main differences occur between different regions, for example, in Asia and Africa, life expectancy depends alot more on 
    #their education (there's a clear correlation ), than in Europe or America (where the plots are more scattered)

#Second question : Is the GNI related to the high income economy of a country, and are they similar between each region?
sns.relplot(data, x='High Income Economy', y='GNI per capita' , col= 'Region')
    #Yes, the GNI per capita is related to high income economy. Only countries with higher GNI values are considered to have high income economy
    #The relation doesnt differ in each region, but we can tell that countires in Europe and America have higher GNI and therefore more are
    #considered to have high income economy. Also, there's no countries in Africa with high enough GNI to have high income economy. 
    
#Third question : Does the international tourism affect the income economy. 
sns.relplot(data, x='High Income Economy', y='International tourism' , col= 'Region')
    #No, there is no correlation between the international tourism and the country's income economy. 

#Fourth question : Does the greenhhouse gas emissions have an effect on female life expectancy?
sns.relplot(data, x='Life expectancy, female', y='Greenhouse gas emissions' , col= 'Region')
    #No, there is no correlation between the two, we can only tell which region have higher gas emissions

#Fifth question :  
sns.relplot(data, x='Population', y='Greenhouse gas emissions' , col= 'Region')

#6th question : 
sns.relplot(data, x='Tertiary education, male', y='GNI per capita' , col= 'Region')


#Part 4.6 

#a)
sns.relplot(data, x='Internet use', y='Greenhouse gas emissions', hue= 'Region')
    # No, there is no clear assosiation in the data, or correlation in the plot

#b)
high_emissions = data[data['Greenhouse gas emissions'] > 0.03]

for i in high_emissions["Country Name"]:
    print(i)
        #The country names are listed in the console

#c)
sns.relplot(data, x='Internet use', y='Greenhouse gas emissions', col= 'Region')
    #There is variation per region, but according to the Internet Use. 
    #For example, in Europe, the internet use is varying on a much smaller scale than in Asia

#d)




# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 08:22:17 2025

@author: Kenya Dacoulis and Carlyn Matar
"""

#-----PART 3-----

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

# gives count, mean, standard deviation, minimum, max and percentiles

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
    

#-----PART 4----- 
import seaborn as sns

#Part 4.1 
sns.relplot(data, x='Life expectancy, female', y='GNI per capita')
sns.relplot(data, x='Life expectancy, male', y='GNI per capita')

#Part 4.2
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
    #These plots are similar to the ones above, with scatter plots, but with additional linear regressions over them for better visualization

#Part 4.5

#First question : Does tertiary education affect male and female life expectancies, and does it differ in each region?
sns.relplot(data, x='Life expectancy, female', y='Tertiary education, female', col= 'Region')
sns.relplot(data, x='Life expectancy, male', y='Tertiary education, male', col= 'Region')
    #Yes, female life expectanciy, in relation to it's tertiary education, has a similar correlation as the for male life expectancy and tertiary education in each region. 
    #The main differences occur between different regions, for example, in Asia and Africa, life expectancy depends alot more on 
    #their education (there's a clear correlation ), than in Europe or America (where the plots are more scattered)

# Second question : Does the number of physicians have an effect on female life expectancy, and does this vary by region and economy level? 
sns.relplot(data, x='Physicians', y='Life expectancy, female', hue= 'High Income Economy', col= 'Region')
    # Yes there is a relationship between female life expectancy and the amount of physicians.
    #High income economy also means more physicians and higher life expectancy



# Third question :  Is the GNI related to the income level of a country, and is it similar between each region?
sns.relplot(data, x='High Income Economy', y='GNI per capita', col= 'Region')
   #Yes, the GNI per capita is related to high income economy. Only countries with higher GNI values are considered to have high income economy
   #The relation doesnt differ in each region, but we can tell that countires in Europe and America have higher GNI and therefore more are
   #considered to have high income economy. Also, there's no countries in Africa with high enough GNI to have high income economy. 
    
       
#Fourth question : Does the income level of a country influence the amount of international tourism and does it vary by region? 
sns.relplot(data, x='High Income Economy', y='International tourism' , col= 'Region')
    #Yes, there is a correlation between a countries income level and the amount international tourism.
    #Those with high income economies have more tourism


#Fifth question : Does the greenhhouse gas emissions have an effect on female life expectancy? 
sns.relplot(data, x='Life expectancy, female', y='Greenhouse gas emissions' , hue ='High Income Economy', col= 'Region') 
    #No, there is no correlation between the two. 
    # It likely has something to do with the income level of countries with high emissions

#Sixth question :  Is there a relationship between Women in national parliament and women's Tertiary education?
sns.relplot(data, x='Women in national parliament', y='Tertiary education, female' , col= 'Region') 
    #It seems to have a clearer correlation in certain regions, like in Oceania where we can see a linear relation,  
    #rather than in Asia or Europe where the scatter plot is forming a cloud like shape. 



#Part 4.6 

#a)
data['emissions per capita'] = data['Greenhouse gas emissions']/ data['Population']

sns.relplot(data, x='Internet use', y='emissions per capita', hue= 'Region')
    # Yes, there is a clear correlation between greenhouse gas emmisions per capita and internet use 

#b)
high_emissions = data[data['emissions per capita'] > 0.03]

for i in high_emissions["Country Name"]:
    print('high emissions per capita =',i)
        #The countries with high emissions per capita are Brunei Darussalam and Qatar

#c)
sns.relplot(high_emissions, x= 'Internet use', y='emissions per capita', hue = 'Region')
    #The only contries with high emissions per capita are Brunei and Qatar. 
    #No variation by region, They are in thesame region, Asia.
    #Little variation in internet use, they have similar, high internet uses.

#d) No, only two countries, Brunei and Qatar have high emissions per capita. 
#   Both countries with high income economies so the countries that do have high emissions are all high economy contries.


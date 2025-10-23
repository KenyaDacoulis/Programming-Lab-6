# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 08:22:17 2025

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

further_info = data.describe ()
print(further_info)

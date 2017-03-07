
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import glob


# # Import all postcodes and district codes

# In[56]:

# check the available files

glob.glob('C:\Git\MyEcho\Economic\postcode_district\Data\CSV\*.csv')[:5]


# In[67]:

# Build dataframe with all postcodes and district codes

path =r'C:\Git\MyEcho\Economic\postcode_district\Data\CSV'

# Build a list of all csv files
all_files = glob.glob(path+'\*.csv')

# import all csv, save as dataframe
df_from_each_file = (pd.read_csv(f, header = None) for f in all_files)
concatenated_df = pd.concat(df_from_each_file, ignore_index = True)

concatenated_df.head()


# In[68]:

# Add headers and clean DataFrame

concatenated_df.columns = ['Postcode', 'PQ', 'EA','NO', 'CY', 'RH', 'LH', 'CC', 'District Code', 'WC']
postcode_district = concatenated_df.drop(concatenated_df.columns[[1,2,3,4,5,6,7,9]], axis = 1)

postcode_district.describe()

# We have more district code than in the income csv file (380 instead of 326)


# # Import Income csv file

# In[78]:

income_path = r'C:\Git\MyEcho\Georgios\deprivationrankings.xlsx'

# Import and clean income file
income = pd.read_excel(income_path)
income = income.drop(income.columns[[3,4,5,6,7,8]], axis = 1)

income.head()


# # Merge both tables and save as csv

# In[90]:

all_data = pd.merge(postcode_district, income,                     left_on = 'District Code', right_on = 'Local Authority District code (2013)')

# Because on merge "inner", only local authority district with ranked income has been kept

all_data = all_data.drop(all_data.columns[[1,2,3]], axis = 1)
all_data.head()


# In[109]:

# Save as csv

all_data.to_csv(r'C:\Git\MyEcho\Economic\database\postcode_incomeRanking.csv', index = False)


# # Postcode look up and average score for income

# In[106]:

postcode = raw_input('Please enter your postcode : ')


# In[107]:

# Put postcode in uppercase
postcode = postcode.upper()

result = all_data['Postcode'] == postcode
all_data[result]


# In[ ]:




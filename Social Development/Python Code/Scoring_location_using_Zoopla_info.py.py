
# coding: utf-8

# In[36]:

import urllib2 as ur
import pandas as pd


# In[37]:

postcode = raw_input('Please enter your postcode: ')


# In[45]:

# Get the district code from the postcode provided
district = postcode[ :4].strip().lower()

# Update the url accordingly
url_district = 'http://www.zoopla.co.uk/house-prices/browse/'+ district +'/'


# In[39]:

# Charge the URL 
response = ur.urlopen(url_district)

html = response.read()


# In[46]:

# Split the html and keep only the average value 
test = html.split('<span class="market-panel-stat-element-value js-market-stats-average-value"\ndata-value-all="')

price = test[1].split(',')[0]


# In[48]:

# Build DataFrame with results

geographic = pd.DataFrame(columns = ['district', 'average'])

geographic.set_value(0, 'district', district)
geographic.set_value(0, 'average', int(price))

# Compute the score for the area. 
# Please note maximum and minimum average prices can be updated 

minP = 20000
maxP = 2500000

geographic['score'] = round((1-(geographic.average - minP)/(maxP- minP)),2)
geographic


# In[ ]:




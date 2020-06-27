#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing Libraries
import requests
import lxml.html as lh
import bs4 as bs
import urllib.request
import numpy as np 
import pandas as pd
from shapely.geometry import Point
import matplotlib.pyplot as plt
import geopandas as gpd
import seaborn as sns


# In[2]:


#Getting the data from url
url = "https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M"
res = requests.get(url)
soup = bs.BeautifulSoup(res.content,'lxml')
table = soup.find_all('table')[0]
df = pd.read_html(str(table))
data = pd.read_json(df[0].to_json(orient='records'))


# In[3]:


#First 5 records
data.head()


# In[4]:


#Choosing only data where field Borough doesn't have not assigned value
raw_data_selected = data[data['Borough'] != 'Not assigned']


# In[5]:


#Grouping Data
raw_data_selected = raw_data_selected.groupby(['Borough', 'Postcode'], as_index=False).agg(','.join)


# In[6]:


#Grouping Data
raw_data_selected = raw_data_selected.groupby(['Borough', 'Postcode'], as_index=False).agg(','.join)


# In[7]:



raw_data_selected.head()


# In[8]:


#Replacing values in Neighbourhood field with Borough where Neighbourhood is not assigned
raw_data_selected['Neighbourhood'] = np.where(raw_data_selected['Neighbourhood'] == 'Not assigned', raw_data_selected['Borough'], raw_data_selected['Neighbourhood'])


# In[9]:


#Grouping Data
raw_data_selected = raw_data_selected.groupby(['Borough', 'Postal Code'], as_index=False).agg(','.join)


# In[10]:


raw_data_selected.head()


# In[11]:


#Replacing values in Neighbourhood field with Borough where Neighbourhood is not assigned
raw_data_selected['Neighbourhood'] = np.where(raw_data_selected['Neighborhood'] == 'Not assigned', raw_data_selected['Borough'], raw_data_selected['Neighbourhood'])


# In[12]:


#Replacing values in Neighbourhood field with Borough where Neighbourhood is not assigned
raw_data_selected['Neighbourhood'] = np.where(raw_data_selected['Neighborhood'] == 'Not assigned', raw_data_selected['Borough'], raw_data_selected['Neighbourhood'])


# In[13]:


#Replacing values in Neighbourhood field with Borough where Neighbourhood is not assigned
raw_data_selected['Neighbourhood'] = np.where(raw_data_selected['Neighborhood'] == 'Not assigned', raw_data_selected['Borough'], raw_data_selected['Neighborhood'])


# In[14]:


raw_data_selected.shape


# In[15]:



Q2: Use the Geocoder package or the csv file to create the following dataframe
So, we are using csv file


# In[16]:


###Q2: Use the Geocoder package or the csv file to create the following dataframe
###So, we are using csv file


# In[17]:


geospatial_url = "https://cocl.us/Geospatial_data"
geospatial_data = pd.read_csv(geospatial_url)


# In[18]:


geospatial_data.head()


# In[19]:


# Renaming the columns
geospatial_data.columns = ['Postal Code', 'Latitude', 'Longitude']


# In[20]:


geospatial_data.columns


# In[21]:


merged_data = pd.merge(raw_data_selected, geospatial_data, on='Postal Code')


# In[22]:


merged_data.head()


# In[ ]:





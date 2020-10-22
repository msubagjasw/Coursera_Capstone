#!/usr/bin/env python
# coding: utf-8

# In[6]:


import requests
from bs4 import BeautifulSoup


# In[13]:


scrap_url = requests.get('https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M').text


# In[14]:


soup = BeautifulSoup(scrap_url,'lxml')


# In[15]:


print(soup.prettify())


# In[50]:


soup.find('table',{'class':'wikitable sortable'}).find_all('td')


# In[97]:


postal_code = []
for xtx in soup.find('table',{'class':'wikitable sortable'}).find_all('td')[0::3]:
    postal_code.append(xtx.contents[0].strip())

postal_code[0:5]


# In[98]:


borough = []
for xtx in soup.find('table',{'class':'wikitable sortable'}).find_all('td')[1::3]:
    borough.append(xtx.contents[0].strip())
    
borough[0:5]


# In[137]:


import numpy as np


# In[161]:


neigh = []
for xtx in soup.find('table',{'class':'wikitable sortable'}).find_all('td')[2::3]:
    neigh.append(xtx.contents[0].strip())
    
neigh[0:5]


# In[105]:


import pandas as pd


# In[205]:


df_toronto = pd.DataFrame({'PostalCode':postal_code, 'Borough':borough, 'Neighborhood':neigh})


# In[166]:


df_toronto.head(12)


# In[173]:


df_toronto.shape


# In[210]:


#df.drop(df[ df['Age'] == 21 ].index, inplace = True) 
df_toronto.drop(df_toronto[df_toronto['Borough'] == 'Not assigned'].index, inplace=True)


# In[212]:


df_toronto.head()


# In[214]:


df_toronto.shape


# In[ ]:





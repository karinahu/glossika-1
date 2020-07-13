#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
df = pd.read_csv("ENG-Collocations10k.csv",encoding= 'unicode_escape', sep ='\t')
df.head()


# In[11]:


df_data=df['node']+' '+df['coll']
df_data.head()


# In[15]:


df['merged'] = df['node']+' '+df['coll']
df.head()


# In[32]:


df_data=df.drop(columns=["nodeID", "node","coll","collPos","preNode","mutInfo","nodePos"])
df_data.loc[:,['freq','merged']] = df_data[['merged', 'freq']]
df_data.columns = ['merged','freq']
df_data.head()


# In[ ]:





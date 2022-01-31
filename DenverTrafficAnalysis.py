#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install matplotlib


# In[2]:


import matplotlib
matplotlib.__version__


# In[3]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import datetime
import time
import seaborn as sns
print('done')


# In[4]:


df = pd.read_csv(r"C:\Users\cjcro\OneDrive\Documents\City_of_Denver_Traffic_Report\Data\traffic_accidents.csv")
df.count()


# In[5]:


df.columns
df = df.drop(columns=['shape', 'incident_id', 'offense_id', 'offense_code',
       'offense_code_extension', 'last_occurrence_date', 'reported_date', 'last_occurrence_date', 'reported_date','HARMFUL_EVENT_SEQ_1', 'HARMFUL_EVENT_SEQ_2',
       'HARMFUL_EVENT_SEQ_3', 'FATALITIES', 'FATALITY_MODE_1', 'district_id', 'neighborhood_id', 'FATALITY_MODE_2', 'SERIOUSLY_INJURED_MODE_1',
       'SERIOUSLY_INJURED_MODE_2',])


# In[6]:


df.head()


# In[7]:


df['FOD'] = pd.to_datetime(df['first_occurrence_date'], format='%Y-%m-%d')

df2013 = df.loc[(df['FOD'] >= '2013-01-01')
               & (df['FOD'] < '2013-12-31')]

df2013_Jan = df.loc[(df['FOD'] >= '2013-01-01')
               & (df['FOD'] < '2013-01-31')]

df201307 = df.loc[(df['FOD'] >= '2013-01-07')
               & (df['FOD'] < '2013-01-07')]
df2013.count()


# In[8]:


df2013total = df2013.groupby(pd.Grouper(key='FOD', axis=0, 
                      freq='m')).count()


# In[9]:


df2013total['first_occurrence_date']


# In[10]:


df.ROAD_CONDITION.unique()


# In[11]:


df2013.ROAD_CONDITION.value_counts()


# In[12]:


df2013_graph = df2013.groupby(pd.Grouper(key='FOD', axis=0, 
                      freq='m')).ROAD_CONDITION.value_counts()


# In[13]:


df2013_graphH = df2013_Jan.groupby(pd.Grouper(key='FOD', axis=0, 
                      freq='H')).count()
dft = df201307.groupby(pd.Grouper(key='FOD', axis=0, 
                      freq='H')).count()
df2013_graphH.first_occurrence_date.mean()


# In[14]:


df2013_graph.plot(x="FOD", y="ROAD_CONDITION", kind="bar", figsize=(20,10))
plt.title("Road Conditions of Accidents 2013", fontsize=25)
plt.ylabel('Accidents')
plt.xlabel('Time/Road Condition')


# In[19]:


df2013_graphH.plot(y="first_occurrence_date", kind="area", figsize=(20,10))
plt.title("Number of Traffic Accidents", fontsize=25)
plt.ylabel('Accidents')
plt.xlabel('Day of Month')


# In[16]:


df2013_graphH


# In[ ]:





# In[17]:


print(dft['first_occurrence_date'])


# In[18]:


print(df2013_graphH['first_occurrence_date'])


# In[ ]:





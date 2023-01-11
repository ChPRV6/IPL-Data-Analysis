#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df=pd.read_csv("IPL_Ball_by_Ball_2022.csv")


# In[3]:


df


# In[4]:


df.head()


# In[5]:


df.info()


# In[6]:


df['batter'].unique()


# In[7]:


df.describe()


# In[8]:


df.iloc[0:3,:]


# In[9]:


df.iloc[:,4:11]


# In[10]:


df['batter'].value_counts()


# In[11]:


df['extra_type'].value_counts()


# In[12]:


df[df['total_run']>2].sort_values(by=['total_run'])


# In[13]:


df.isnull()


# In[14]:


df.pop(item='player_out')
df.pop(item='kind')
df.pop(item='fielders_involved')
print(df)


# In[15]:


df['ID'].div(10)


# In[16]:


df.where(df['bowler']=='DJ Bravo')


# In[21]:


df[df['total_run'].between(2,6)].sort_values(by=['total_run'])


# In[23]:


df[(df['total_run']>2) & (df['total_run']<=5)]


# In[24]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[25]:


x=df["innings"]
y=df["total_run"]


# In[27]:


plt.plot(x,y,'c',linestyle='dashed',linewidth=1.5,markersize=8)
plt.xlabel('Innings -->')
plt.ylabel('Total Runs -->')
plt.title('Information Regarding Innings vs Total Runs Scored')


# In[ ]:





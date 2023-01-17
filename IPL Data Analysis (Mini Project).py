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


# In[17]:


df[df['total_run'].between(2,6)].sort_values(by=['total_run'])


# In[18]:


df[(df['total_run']>2) & (df['total_run']<=5)]


# In[19]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[20]:


x=df["innings"]
y=df["total_run"]


# In[21]:


plt.plot(x,y,'c',linestyle='dashed',linewidth=1.5,markersize=8)
plt.xlabel('Innings -->')
plt.ylabel('Total Runs -->')
plt.title('Information Regarding Innings vs Total Runs Scored')


# In[22]:


#RUNS=df['total_run']
#lava= [0, 1, 2, 3, 4, 5, 6]
#plt.pie(RUNS,autopct='%1.1f%%')
#plt.show()
df.head()


# In[23]:


sns.displot(df['total_run'])


# In[24]:


sns.displot(df['BattingTeam'])


# In[25]:


#run=df['total_run']
#x=np.array([0,1,2,3,4,5])
#plt.pie(run,labels=x)
#plt.show()
sns.jointplot(x='total_run',y='bowler',data=df)


# In[26]:


df['bowler'].unique()


# In[27]:


bowler=df['bowler'].unique()
plt.plot(bowler)


# In[28]:


import collections 


# In[29]:


def counter(Arr):
    return collections.Counter(Arr)


# In[30]:


scores=df['total_run']
scoring=counter(scores)
scoring_zone=[]
keys=[]
for (key,value) in scoring.items():
    scoring_zone.append(value)
    keys.append(key)
print(keys)
plt.pie(scoring_zone,labels=keys,autopct='%1.1f%%',explode=[0,0,0,0,0.35,0.3,0,0.8],shadow=True)


# In[31]:


sns.pairplot(df)


# In[32]:


sns.countplot('batter',data=df)


# In[33]:


sns.countplot('BattingTeam',data=df)


# In[ ]:





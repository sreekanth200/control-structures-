#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[2]:


df=sns.load_dataset('tips')


# In[3]:


df


# In[4]:


df.columns


# In[5]:


df.isna().sum()


# In[6]:


sns.heatmap(df.isna())


# In[7]:


df=sns.load_dataset("healthexp")


# In[8]:


df


# In[9]:


df.describe()


# In[10]:


df.isna().sum()


# In[11]:


sns.heatmap(df.isna())


# In[12]:


import numpy as np
import pandas as pd
import seaborn as sns


# In[13]:


df=sns.load_dataset("tips")


# In[14]:


df.head()


# In[15]:


#### a continous variables
import matplotlib.pyplot as plt
plt.hist(df['total_bill'],color='r')
#sns.histoplot(df['total_bill'])


# In[16]:


df.head()


# In[17]:


df.shape


# In[18]:


sns.rugplot(df['total_bill'].sample(20))


# In[19]:


sns.jointplot(x="total_bill",y="tip",data=df,color="r")


# In[20]:


sns.jointplot(x='total_bill',y='tip',data=df,color='r',kind='reg')


# In[21]:


sns.jointplot(x='total_bill',y='tip',data=df,color='r',kind='hex')


# In[22]:


sns.jointplot(x='total_bill',y='tip',data=df,color='r',kind='kde')


# In[23]:


df.head()


# In[24]:


df.columns


# In[25]:


sns.barplot(x='day',y='tip',data=df)


# In[26]:


sns.violinplot(x='day',y='tip',data=df)


# In[27]:


sns.stripplot(x='day',y='tip',data=df)


# In[28]:


sns.swarmplot(x='day',y='tip',data=df)


# In[29]:


plt.figure(figsize=(10,10))
plt.subplot(2,2,1)
sns.barplot(x='day',y='tip',data=df)
plt.subplot(2,2,2)
sns.swarmplot(x='day',y='tip',data=df)
plt.subplot(2,2,3)
sns.stripplot(x='day',y='tip',data=df)
plt.subplot(2,2,4)
sns.violinplot(x='day',y='tip',data=df)
plt.savefig("sample.jpg")


# In[31]:


jointgrid
pairgrid
facetgrid ### important from visualizations


# In[32]:


sns.jointplot(x='total_bill',y='tip',data=df,color='r',kind='reg')


# In[33]:


g=sns.JointGrid(x='total_bill',y='tip',data=df)
g.plot(sns.scatterplot,sns.histplot)


# In[34]:


#### pairgrid
#### pairplot
#### pairgrid


# In[35]:


### pair plot is draw between numerical columns

sns.pairplot(df)


# In[36]:


g=sns.PairGrid(df)
g.map_diag(sns.rugplot)
g.map_lower(sns.kdeplot)
g.map_upper(sns.regplot,color='r')


# In[38]:


df=sns.load_dataset("healthexp")


# In[39]:


df


# In[40]:


df.shape


# In[41]:


df.head


# In[42]:


df.head(5)


# In[43]:


###a continous variables
import matplotlib.pyplot as plt


# In[44]:


df["Country"].hist(color="r")
plt.title("Histogram of 'country'")
plt.xlabel("Country")
plt.ylabel("Frequency")
plt.show()


# In[2]:


sns.jointplot(x='count',y='tip',data=df,color='r',kind='reg')


# In[48]:


df=sns.color_palette()


# In[49]:


df


# In[ ]:


df=sns.


# In[2]:


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# Load the dataset
titanic = sns.load_dataset("titanic")


# In[3]:


titanic


# In[4]:


# 1. Bar plot of survival rate by sex
survived_sex = titanic.groupby('sex')['survived'].mean()
survived_sex.plot(kind='bar')
plt.title('Survival Rate by Sex')
plt.ylabel('Survival Rate')
plt.show()


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
data = pd.read_csv('C:/Users/sneha/Downloads/netflix_titles.csv')


# In[5]:


#basic info
data.head()


# In[6]:


#no of rows nd cols
data.shape


# In[7]:


#total elements
data.size


# In[9]:


data.columns


# In[10]:


data.dtypes


# In[11]:


#info to show all details
data.info()


# In[13]:


#remove any duplicates data.drop_duplicates(inplace=True),inplace to make the change permanent
data[data.duplicated()]


# In[18]:


#check null
data.isnull().sum()


# In[19]:


import seaborn as sns
sns.heatmap(data.isnull())


# In[22]:


data[data['title'].str.contains('House of Cards')]


# In[31]:


#groupby
data.groupby('type').type.count()


# In[33]:


sns.countplot(data['type'])


# In[36]:


data.info()


# In[37]:


data['release_year']=data['release_year'].dt.year


# In[38]:


data.info()


# In[45]:


#find movie names released 
data[(data['type']=='Movie') & (data['release_year']==2016)]


# In[47]:


data[(data['country']=='India') & (data['type']=='TV Show')]['title']


# In[48]:


data['director'].value_counts().head(5)


# In[51]:


#different ratings nunique for count
data['rating'].unique()


# In[54]:


data[(data['rating']=='TV-14') & (data['type']=='Movie')].shape


# In[59]:


data.head(5)


# In[63]:


data[['Minutes','Unit']]=data['duration'].str.split(' ',expand=True)


# In[64]:


data.head(5)


# In[66]:


data['Minutes'].max()


# In[70]:


#country with highest tv shows
data_tvshow=data[data['type']=='TV Show']
data_tvshow.country.value_counts().head(1)


# In[76]:


#sort by year
data.sort_values(by='release_year',ascending=True)


# In[ ]:





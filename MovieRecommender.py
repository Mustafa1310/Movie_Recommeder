#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


column_names = ['user_id', 'item_id', 'rating', 'timestamp']
df = pd.read_csv('u.data', sep='\t', names=column_names)


# In[4]:


df.head()


# In[5]:


movie_titles = pd.read_csv("Movie_Id_Titles")
movie_titles.head()


# In[6]:


df=pd.merge(df,movie_titles,on='item_id')


# In[7]:


df.head()


# In[8]:


import matplotlib.pyplot as plt


# In[9]:


import seaborn as sns


# In[11]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[12]:


df.groupby('title')['rating'].mean().sort_values(ascending=False).head()


# In[13]:


df.groupby('title')['rating'].count().sort_values(ascending=False).head()


# In[25]:


ratings = pd.DataFrame(df.groupby('title')['rating'].mean())


# In[26]:


ratings.head()


# In[27]:


ratings['num of ratings'] = pd.DataFrame(df.groupby('title')['rating'].count().sort_values(ascending=False))


# In[28]:


ratings.head()


# In[29]:


plt.figure(figsize=(10,4))
ratings['num of ratings'].hist(bins=70)


# In[30]:


plt.figure(figsize=(10,4))
ratings['rating'].hist(bins=70)


# In[31]:


sns.jointplot(x='rating',y='num of ratings',data=ratings,alpha=0.5)


# In[32]:


moviemat = df.pivot_table(index='user_id',columns='title',values='rating')


# In[33]:


moviemat.head()


# In[34]:


ratings.sort_values('num of ratings',ascending=False).head(10)


# In[35]:


ratings.head()


# In[36]:


starwars_user_ratings = moviemat['Star Wars (1977)']


# In[38]:


starwars_user_ratings.head()


# In[39]:


liarliar_user_ratings = moviemat['Liar Liar (1997)']


# In[40]:


liarliar_user_ratings.head()


# In[41]:


similar_to_starwars = moviemat.corrwith(starwars_user_ratings)


# In[42]:


similar_to_liarliar = moviemat.corrwith(liarliar_user_ratings)


# In[43]:


corr_starwars = pd.DataFrame(similar_to_starwars,columns=['Correlation'])
corr_starwars.dropna(inplace=True)
corr_starwars.head()


# In[45]:


corr_starwars.sort_values('Correlation',ascending=False).head(10)


# In[46]:


corr_starwars = corr_starwars.join(ratings['num of ratings'])
corr_starwars.head()


# In[47]:


corr_starwars[corr_starwars['num of ratings']>100].sort_values('Correlation',ascending=False).head()


# In[48]:


corr_liarliar = pd.DataFrame(similar_to_liarliar,columns=['Correlation'])
corr_liarliar.dropna(inplace=True)
corr_liarliar = corr_liarliar.join(ratings['num of ratings'])
corr_liarliar[corr_liarliar['num of ratings']>100].sort_values('Correlation',ascending=False).head()


# In[50]:


conair_user_ratings = moviemat['Con Air (1997)']


# In[51]:


conair_user_ratings.head()


# In[52]:


similar_to_conair = moviemat.corrwith(conair_user_ratings)
corr_conair = pd.DataFrame(similar_to_conair,columns=['Correlation'])
corr_conair.dropna(inplace=True)
corr_conair.head()


# In[53]:


corr_conair = corr_conair.join(ratings['num of ratings'])
corr_conair.head()


# In[56]:


corr_conair[corr_conair['num of ratings']>100].sort_values('Correlation',ascending=False).head()


# In[ ]:





# In[58]:





# In[ ]:





# In[ ]:





# In[ ]:





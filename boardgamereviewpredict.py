#!/usr/bin/env python
# coding: utf-8

# In[9]:


import seaborn as sns
import sklearn


# In[10]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


# In[12]:


df=pd.read_csv("games.csv")


# In[13]:


df.head()


# In[39]:


plt.hist(df["average_weight"])
plt.show()


# In[18]:


print(df[df["average_rating"]==0].iloc[0])

print(df[df["average_rating"]>0].iloc[0])


# In[19]:


df=df[df["users_rated"]>0]

df=df.dropna(axis=0)


# In[20]:


plt.hist(df["average_rating"])
plt.show()


# In[21]:



#correlation matrix
corrmat = df.corr()
fig = plt.figure(figsize=(12,9))

sns.heatmap(corrmat, vmax=.8,square=True)
plt.show()


# In[22]:


columns = df.columns.tolist()

columns = [c for c in columns if c not in["bayes_average_rating","average_rating","type","name","id"]]

target = "average_rating"


# In[24]:


train=df.sample(frac=0.8,random_state=1)

#select anything not in the training set and put it in test
test=df.loc[~df.index.isin(train.index)]

print(train.shape)
print(test.shape)


# In[27]:


from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

LR = LinearRegression()

LR.fit(train[columns], train[target])


# In[30]:


predictions = LR.predict(test[columns])
mean_squared_error(predictions, test[target])


# In[32]:


# importing random forest model

from sklearn.ensemble import RandomForestRegressor

RFR = RandomForestRegressor(n_estimators=100, min_samples_leaf=10, random_state=1)
RFR.fit(train[columns], train[target])


# In[33]:


predictions = RFR.predict(test[columns])

mean_squared_error(predictions, test[target])


# 

# In[35]:


test[columns].iloc[0]


# In[37]:


#predictions with both models
rating_LR = LR.predict(test[columns].iloc[0].values.reshape(1,-1))
rating_RFR = RFR.predict(test[columns].iloc[0].values.reshape(1,-1))

print(rating_LR)
print(rating_RFR)


# In[38]:


test[target].iloc[0]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





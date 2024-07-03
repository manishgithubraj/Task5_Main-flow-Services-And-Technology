#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = pd.read_csv('C:\\Users\\ASUS\\Downloads\\heart.csv')


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.columns.values


# In[6]:


df.isna().sum()


# In[7]:


df.info()


# In[8]:


df.hist(bins = 50, grid = False, figsize=(20,15));


# In[9]:


df.describe()


# In[10]:


Questions = ["1. How many people have heart disease and how many people doesn't have heart disease?",
             "2. People of which sex has most heart disease?",
             "3. People of which sex has which type of chest pain most?",
             "4. People with which chest pain are most pron to have heart disease?"]
Questions


# In[11]:


df.target.value_counts()


# In[12]:


df.target.value_counts().plot(kind = 'bar', color=["orchid", "salmon"])
plt.title("Heart Disease Values")
plt.xlabel("1 = Heart Disease, 0 = No heart Disease")
plt.ylabel("Amount");


# In[13]:


df.target.value_counts().plot(kind = 'pie', figsize = (8, 6))
plt.legend(["Disease", "No Disease"]);


# In[14]:


df.sex.value_counts()


# In[15]:


df.sex.value_counts().plot(kind = 'pie', figsize = (8, 6))
plt.title('Male Female ratio')
plt.legend(["Male", "Female"]);


# In[16]:


pd.crosstab(df.target, df.sex)


# In[17]:


sns.countplot(x = 'target', data = df, hue = 'sex')
plt.title("Heart Disease Frequency for Sex")
plt.xlabel("0 = No Heart Disease, 1 = heart Disease");


# In[18]:


df.cp.value_counts()


# In[19]:


pd.crosstab(df.sex, df.cp)


# In[20]:


pd.crosstab(df.sex, df.cp).plot(kind = "bar", color = ["coral", "lightskyblue", "plum", "khaki"])
plt.title("Type of Chest Pain for Sex")
plt.xlabel("0 = Female, 1 = Male");


# In[21]:


pd.crosstab(df.cp, df.target)


# In[22]:


sns.countplot(x = "cp", data = df, hue = "target");


# In[23]:


sns.displot(x = "age", data = df, bins = 30, kde = True);


# In[24]:


sns.displot(x = "thalach", data = df, bins = 30, kde = True, color = 'chocolate');


# In[ ]:





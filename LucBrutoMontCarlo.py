#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[5]:


rev_m = 170
rev_stdev = 20
iterations = 1000


# In[6]:


rev = np.random.normal(rev_m,rev_stdev,iterations)
rev


# In[7]:


plt.figure(figsize=(15,6))
plt.plot(rev)
plt.show()


# In[8]:


COGS = - (rev*np.random.normal(0.6,0.1))
plt.figure(figsize=(15,6))
plt.plot(COGS)
plt.show()


# In[9]:


COGS.mean()


# In[10]:


COGS.std()


# In[12]:


gross_profit = rev + COGS
gross_profit
plt.figure(figsize=(15,6))
plt.plot(gross_profit)
plt.show()


# In[13]:


max(gross_profit)


# In[14]:


min(gross_profit)


# In[15]:


gross_profit.mean()


# In[16]:


gross_profit.std()


# In[17]:


plt.figure(figsize=(15,6))
plt.hist(gross_profit,bins =[40,50,60,70,80,90,100,110,120])
plt.show()


# In[18]:


#mais facil
plt.figure(figsize=(15,6))
plt.hist(gross_profit,bins =20)
plt.show()


# In[ ]:





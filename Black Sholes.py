#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
from pandas_datareader import data as wb
from scipy.stats import norm


# In[15]:


def d1(S, K, r, stdev, T):
    return (np.log(S / K) + (r + stdev ** 2 / 2) * T) / (stdev * np.sqrt(T))
def d2(S, K, r, stdev, T):
    return (np.log(S / K) + (r - stdev ** 2 / 2) * T) / (stdev * np.sqrt(T))


# In[16]:


def BSM(S, K, r, stdev, T):
    return (S * norm.cdf(d1(S, K, r, stdev, T))) - (K * np.exp(-r * T) * norm.cdf(d2(S, K, r, stdev, T)))


# In[19]:


ticker = 'BOVA11.SA'
data = pd.DataFrame()
data[ticker] = wb.DataReader(ticker, data_source = 'yahoo', start = '2007-1-1')['Adj Close']


# In[20]:


S = data.iloc[-1]
S


# In[21]:


log_returns = np.log(1 + data.pct_change())


# In[22]:


stdev = log_returns.std() * 250 ** 0.5
stdev


# In[23]:


r = 0.025
K = 110.0
T = 1


# In[24]:


d1(S, K, r, stdev, T)


# In[25]:


d2(S, K, r, stdev, T)


# In[26]:


#Preço da opção de compra
BSM(S, K, r, stdev, T)


# In[ ]:





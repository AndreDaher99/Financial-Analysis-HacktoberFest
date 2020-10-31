#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
from scipy.stats import norm
get_ipython().run_line_magic('matplotlib', 'inline')


# In[22]:


acao = 'BOVA11.SA'
mydata = pd.DataFrame()
mydata[acao] = wb.DataReader(acao, data_source='yahoo',start = '2010-1-1')['Adj Close']
mydata.tail()


# In[27]:


#retornos simples de um conjunto de dados
log_returns = np.log(1 + mydata.pct_change())


# In[28]:


log_returns.tail()


# In[29]:


mydata.plot(figsize=(15,6))


# In[30]:


log_returns.plot(figsize=(15,6))


# In[32]:


u = log_returns.mean()
u


# In[33]:


var = log_returns.var()
var


# In[34]:


drift = u - (0.5 * var)
drift


# In[35]:


stdev = log_returns.std()
stdev


# In[38]:


np.array(drift)


# In[39]:


drift.values


# In[40]:


stdev.values


# In[42]:


#numero de desvios padroes de acordo com a %
norm.ppf(0.95)


# In[43]:


x = np.random.rand(10,2)
x


# In[44]:


norm.ppf(x)


# In[45]:


z = norm.ppf(np.random.rand(10,2))
z


# In[46]:


t_intervals = 1000
iterations = 10


# In[47]:


daily_returns = np.exp(drift.values + stdev.values * norm.ppf(np.random.rand(t_intervals,iterations)))


# In[48]:


daily_returns


# In[49]:


#ultimo valor da ação
s0 = mydata.iloc[-1]
s0


# In[50]:


#matriz de zeros do tamanho da outra
price_list = np.zeros_like(daily_returns)


# In[51]:


price_list


# In[52]:


price_list[0] = s0
price_list


# In[53]:


for t in range(1,t_intervals):
    price_list[t] = price_list[t-1] * daily_returns[t]


# In[54]:


price_list


# In[55]:


plt.figure(figsize=(15,6))
plt.plot(price_list)


# In[ ]:





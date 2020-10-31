#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as wb


# In[18]:


tickers = ['ABEV3.SA','ITUB4.SA']
mydata = pd.DataFrame()

for t in tickers:
    mydata[t]=wb.DataReader(t,data_source='yahoo',start ='2018-1-1')['Adj Close']
(mydata/mydata.iloc[0]*100).plot()    


# In[3]:


returns = (mydata/mydata.shift(1))-1
returns


# In[4]:


returns.mean()*250


# In[5]:


returns.cov()*250


# In[6]:


returns.corr()


# In[7]:


pesos = [0.4,0.6]
weights = np.array(pesos)


# In[8]:


np.sum(weights * returns.mean())*250


# In[9]:


np.dot(weights.T,np.dot(returns.cov()*250,weights))


# In[10]:


np.sqrt(np.dot(weights.T,np.dot(returns.cov()*250,weights)))


# In[11]:


num_tickers = len(tickers)
num_tickers


# In[12]:


pfolio_returns =[]
pfolio_volatilities=[]
for x in range(1000):
    weights = np.random.random(num_tickers)
    weights /= np.sum(weights)
    pfolio_returns.append(np.sum(weights*returns.mean())*250)
    pfolio_volatilities.append(np.sqrt(np.dot(weights.T,np.dot(returns.cov()*250,weights))))

pfolio_returns,pfolio_volatilities


# In[13]:


pfolio_returns =[]
pfolio_volatilities=[]
for x in range(1000):
    weights = np.random.random(num_tickers)
    weights /= np.sum(weights)
    pfolio_returns.append(np.sum(weights*returns.mean())*250)
    pfolio_volatilities.append(np.sqrt(np.dot(weights.T,np.dot(returns.cov()*250,weights))))
pfolio_returns = np.array(pfolio_returns)
pfolio_volatilities = np.array(pfolio_volatilities)
pfolio_returns,pfolio_volatilities


# In[14]:


portfolios = pd.DataFrame({'Return':pfolio_returns,'Volatility':pfolio_volatilities})


# In[15]:


portfolios.head()


# In[16]:


portfolios.tail()


# In[17]:


portfolios.plot(x='Volatility',y='Return',kind='scatter',figsize=(12,8))
plt.xlabel=('Expected Volatility')
plt.ylabel=('Expected Return')


# In[ ]:





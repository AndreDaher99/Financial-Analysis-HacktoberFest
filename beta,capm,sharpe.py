#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas_datareader import data as wb


# In[13]:


tickers = ['^BVSP','OIBR3.SA']
mydata = pd.DataFrame()
for t in tickers:
    mydata[t]=wb.DataReader(t, data_source='yahoo',start='2012-1-1',end = '2019-12-31')['Adj Close']
mydata


# In[14]:


returns = np.log(mydata/mydata.shift(1))


# In[15]:


cov = returns.cov()*250
cov


# In[16]:


cov_market = cov.iloc[0,1]
cov_market


# In[17]:


market_var = returns['^BVSP'].var()*250
market_var


# In[18]:


beta = cov_market/market_var
beta


# In[20]:


capm = 0.025+beta * 0.05
capm


# In[22]:


sharpe = (capm-0.025)/(returns['OIBR3.SA'].std()*250**0.5)
sharpe


# In[ ]:





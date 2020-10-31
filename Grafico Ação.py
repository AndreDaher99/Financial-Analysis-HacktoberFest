#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt


# In[2]:


tickers = ['BOVA11.SA','VVAR3.SA','OIBR3.SA','MGLU3.SA']
mydata = pd.DataFrame()
for t in tickers:
    mydata[t]=wb.DataReader(t,data_source = 'yahoo', start = '2017-9-1')['Adj Close']


# In[4]:


mydata.info()


# In[14]:


mydata.head()


# In[6]:


mydata.tail()


# In[3]:


(mydata/mydata.iloc[0]*100).plot()
plt.show()


# In[16]:


mydata.plot()
plt.show()


# In[4]:


returns = (mydata/mydata.shift(1))-1
returns


# In[18]:


weights = ([0.25,0.25,0.25,0.25])
np.dot(returns, weights)


# In[5]:


annual_returns = returns.mean()*250
annual_returns


# In[6]:


np.dot(annual_returns, weights)
print('Taxa de Retorno Anual: %.3f%s'%(np.dot(annual_returns, weights)*100,'%'))


# In[ ]:





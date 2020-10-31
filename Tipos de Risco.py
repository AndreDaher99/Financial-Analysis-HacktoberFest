#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as wb


# In[3]:


tickers = ['^BVSP','VVAR3.SA']
mydata = pd.DataFrame()
for t in tickers:
    mydata[t]=wb.DataReader(t, data_source='yahoo',start = '2019-1-1')['Adj Close']

returns = (mydata/mydata.shift(1))-1
returns


# In[9]:


returns['^BVSP'].mean()


# In[10]:


returns['^BVSP'].mean()*250


# In[11]:


returns['^BVSP'].std()


# In[12]:


returns['^BVSP'].std()*250**0.5


# In[13]:


returns['VVAR3.SA'].mean()


# In[14]:


returns['VVAR3.SA'].mean()*250


# In[16]:


returns['VVAR3.SA'].std()


# In[17]:


returns['VVAR3.SA'].std()*250**0.5


# In[18]:


mydata['VVAR3.SA'].plot()
plt.show()


# In[18]:


returns


# In[20]:


var = returns.var()
var


# In[22]:


var_a = returns['BOVA11.SA'].var()*250
var_a


# In[24]:


cov = returns.cov()
cov


# In[29]:


cov_a = returns.cov()*250
round(cov_a*100,2)


# In[34]:


corr=returns.corr()
round(corr*100,2)


# In[42]:


weights = np.array([0.5,0.5])
pt_var = np.dot(weights.T,np.dot(returns.cov()*250,weights))
print('Variância: %.2f%s'%(pt_var*100,'%'))


# In[38]:


pt_vol = pt_var ** 0.5
pt_vol


# In[40]:


pt_vol = (np.dot(weights.T,np.dot(returns.cov()*250,weights)))**0.5
print('Volatilidade: %.2f%s'%(pt_vol*100,'%'))


# In[48]:


var_a_1 = returns['BOVA11.SA'].var()*250
var_a_1


# In[49]:


var_a_2 = returns['ITUB4.SA'].var()*250
var_a_2


# In[50]:


rd = pt_var - (weights[0]**2*var_a_1) - (weights[1]**2*var_a_2)
rd


# In[51]:


print('Risco Diversificável: %.2f%s'%(rd*100,'%'))


# In[10]:


nrd = pt_var - rd
nrd *100


# In[54]:


pt_var == rd+nrd


# In[ ]:





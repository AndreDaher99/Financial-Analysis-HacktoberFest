#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pandas_datareader import data as wb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
acao1=input('CODE: ')
acao2=input('CODE: ')
L=[acao1,acao2]

a = wb.DataReader(acao1, data_source = 'yahoo', start = '2017-8-1')
b = wb.DataReader(acao2, data_source = 'yahoo', start = '2017-8-1')
c = pd.DataFrame()
for t in L:
    c[t] = wb.DataReader(t, data_source = 'yahoo', start = '2017-8-1')['Adj Close']


a['Retorno Simples']=((a['Adj Close']/a['Adj Close'].shift(1))-1)*100
b['Retorno Simples 2']=((b['Adj Close']/b['Adj Close'].shift(1))-1)*100


# In[2]:


a['Retorno Simples'].plot(color='black',title = 'Variação Diária: %s'%(acao1))
plt.show()
b['Retorno Simples 2'].plot(color='red',title = 'Variação Diária: %s'%(acao2))
plt.show()

avg_returns_d_1=a['Retorno Simples'].mean()
print('Média de Variação Diária %s: %.3f%s'%(acao1,avg_returns_d_1, '%'))
avg_returns_d_2=b['Retorno Simples 2'].mean()
print('Média de Variação Diária %s: %.3f%s'%(acao2,avg_returns_d_2, '%'))

avg_returns_d_1=a['Retorno Simples'].mean()*250
print('\nMédia de Variação Anual %s: %.3f%s'%(acao1,avg_returns_d_1,'%'))
avg_returns_d_2=b['Retorno Simples 2'].mean()*250
print('Média de Variação Anual %s: %.3f%s'%(acao2,avg_returns_d_2,'%'))


# In[3]:


a['Adj Close'].plot(color='black',title=('%s')%(acao1))
plt.show()
b['Adj Close'].plot(color='red',title=('%s')%(acao2))
plt.show()
(c/c.iloc[0]*100).plot(color=('black','red'), title = 'Comparativo ')
plt.show()


# In[ ]:





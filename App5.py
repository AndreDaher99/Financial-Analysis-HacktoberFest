import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as wb

Lnome = []
Lquant = []
soma = 0
Lpesos = []

Datai = input('Start: ')
Dataf = input('End: ')
for c in range(2):
    nome = input('Code: ')
    carteira = int(input('Quantity: '))
    Lnome.append(nome)
    Lquant.append(carteira)
    soma+=carteira
for x in Lquant:
    Lpesos.append(x/soma)    
mydata = pd.DataFrame()

for n in Lnome:
    mydata[n]=wb.DataReader(n,data_source='yahoo',start = Datai, end = Dataf)['Adj Close']

returns = (mydata/mydata.shift(1))-1
returns.mean()*250
returns.cov()*250
returns.corr()
weights = np.array(Lpesos)
np.sum(weights * returns.mean())*250
np.dot(weights.T,np.dot(returns.cov()*250,weights))
np.sqrt(np.dot(weights.T,np.dot(returns.cov()*250,weights)))
num_tickers = 2

    
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




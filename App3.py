import pandas as pd
import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt


Lnome = []
Lquant = []
soma = 0
Lpesos = []

quantidade = int(input('Total: '))
Datai = input('Start: ')
Dataf = input('End: ')
for c in range(1,quantidade + 1):
    nome = input('Code: ')
    carteira = int(input('Quantity: '))
    Lnome.append(nome)
    Lquant.append(carteira)
    soma+=carteira
for x in Lquant:
    Lpesos.append(x/soma)   

data = pd.DataFrame()
for n in Lnome:
    data[n] = wb.DataReader(n, data_source = 'yahoo', start = Datai, end = Dataf)['Adj Close']

returns = (data/data.shift(1)) - 1
weights = np.array(Lpesos)
annual_returns = returns.mean() * 250
result = np.dot(annual_returns, weights)
cov = returns.cov()
a = data.iloc[0]
b = data.iloc[-1]

total_return = (b/a)-1
portfolio_return = np.dot(total_return, weights)
portfolio_vol = (np.dot(weights.T,np.dot(returns.cov()*250,weights))) ** 0.5
print(data)

print('\nAverage Return (Annual): %.3f%s'%(result*100,'%'))

print('\nVolatility (Annual): %.3f%s'%(portfolio_vol*100,'%'))

print('\nTotal Return Portfolio: %.3f%s'%(portfolio_return*100,'%'))

print(total_return)



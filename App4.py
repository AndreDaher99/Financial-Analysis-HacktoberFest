import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
from scipy.stats import norm

acao = input('Code: ')
Datai = input('Start: ')
Dataf = input('End: ')
mydata = pd.DataFrame()
mydata[acao] = wb.DataReader(acao, data_source='yahoo',start = Datai, end = Dataf)['Adj Close']

log_returns = np.log(1 + mydata.pct_change())
u = log_returns.mean()
var = log_returns.var()
drift = u - (0.5 * var)
stdev = log_returns.std()
np.array(drift)
x = np.random.rand(10,2)
norm.ppf(x)
z = norm.ppf(np.random.rand(10,2))
t_intervals = 1000
iterations = 10
daily_returns = np.exp(drift.values + stdev.values * norm.ppf(np.random.rand(t_intervals,iterations)))
s0 = mydata.iloc[-1]
price_list = np.zeros_like(daily_returns)
price_list[0] = s0
for t in range(1,t_intervals):
    price_list[t] = price_list[t-1] * daily_returns[t]


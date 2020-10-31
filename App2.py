import pandas as pd
import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

nome = input('Code: ')
Datai = input('Start: ')
Dataf = input('End: ')

data = pd.DataFrame()
data[nome] = wb.DataReader(nome, data_source = 'yahoo', start = Datai, end = Dataf)['Adj Close']

d_return = (data/data.shift(1))-1
d_return

avg_return_d = d_return.mean()
avg_return_a = d_return.mean() * 250

stdev_d = d_return.std()
stdev_a = d_return.std()*250**0.5

a = data.iloc[0]
b = data.iloc[-1]

total = ((b/a)-1)*100 

print(data)
print('\nAverage Return (Daily): %.3f%s'%(avg_return_d*100, '%'))
print('\nAverage Return (Annual): %.3f%s'%(avg_return_a*100, '%'))
print('\nVolatility (Daily): %.3f%s'%(stdev_d*100, '%'))
print('\nVolatility (Annual): %.3f%s'%(stdev_a*100, '%'))
print('\nTotal Return: %.2f%s'%(total,'%'))

    
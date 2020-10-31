import pandas as pd
import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

nome = input('Code: ')
Datai = input('Start: ')
Dataf = input('End: ')


acao = wb.DataReader(nome, data_source = 'yahoo', start = Datai, end = Dataf)['Adj Close']
print(acao)
    


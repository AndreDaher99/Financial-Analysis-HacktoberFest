import json

import pandas as pd
from pandas_datareader import data as wb

class StockService:

    @classmethod
    def get_all_info(cls, symbol, start_date, end_date):
        data = pd.DataFrame()
        data[symbol] = wb.DataReader(symbol, data_source = 'yahoo', start = start_date, end = end_date)['Adj Close']

        d_return = (data[symbol]/data[symbol].shift(1)) - 1
        historical_data = []
        for date, value in d_return.iteritems():
            historical_data.append({
                'date': date,
                'value': value
            })

        avg_return_d = d_return.mean()
        avg_return_a = d_return.mean() * 250

        stdev_d = d_return.std()
        stdev_a = d_return.std()*250**0.5

        a = data[symbol].iloc[0]
        b = data[symbol].iloc[-1]

        total = ((b/a)-1)*100 

        return {
            'historical_data': historical_data,
            'average_daily_returns': avg_return_d * 100,
            'average_annual_returns': avg_return_a * 100,
            'daily_stdev': stdev_d * 100,
            'annual_stdev': stdev_a * 100,
            'total_return': total
        }

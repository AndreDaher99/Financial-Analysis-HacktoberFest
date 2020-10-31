import datetime
from flask import Flask, request

from services.stock import StockService

app = Flask(__name__)

def one_year_ago_date():
    one_year_ago_datetime = datetime.datetime.now() - datetime.timedelta(days=365)
    return one_year_ago_datetime.date()

def today_date():
    return datetime.datetime.now().date()

@app.route('/stock')
def get():
    symbol = request.args.get('symbol')
    start_date = request.args.get('start_date', default=one_year_ago_date())
    end_date = request.args.get('end_date', default=today_date())
    
    stock_info = StockService.get_all_info(symbol, start_date, end_date)
    print(stock_info)
    return stock_info

if __name__ == '__main__':
    app.run()

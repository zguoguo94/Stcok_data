import yfinance as yf
from datetime import datetime, date, time, timedelta

def getData(name, start, end, interval):
    stock = yf.Ticker(name)
    return stock.history(start=start, end=end, interval= interval)

start = datetime(2019, 11, 8)
end = start + timedelta(days=1)
stocks = ['GOOG','AAPL', 'MSFT', 'AMZN', 'INTC', 'JPM', 'BAC', 'HSBC', 'C', 'GS', 'PNC', 'WMT', 'TGT','JCP','KSS', 'HD', 'PFE','MRK','JNJ','ABBV','BMY','TPR','AEO','GES','CPRI','TIF']
for i in stocks:
    data = getData(i, start, end, "1m")
    data.name = f'{i}.csv'
    data.to_csv(data.name)
    

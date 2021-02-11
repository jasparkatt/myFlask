# this is using the alpha_vantage wrapper python package...not quite the same as using the api directly as code below
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt

key = 'LAJBI8EN52GC18OY'
ts = TimeSeries(key, output_format='pandas')
ti = TechIndicators(key)

aapl_data, aapl_meta_data = ts.get_daily(symbol='GME')
aapl_sma, aapl_meta_sma = ti.get_sma(symbol='GME')

figure(num=None, figsize=(15, 6), dpi=80, facecolor='w', edgecolor='k')
aapl_data['4. close'].plot()
plt.tight_layout()
plt.grid()
plt.show()

# this is using the actual api from alphavantage to get the data from the url api
import requests
import json
from pprint import pprint
key = 'LAJBI8EN52GC18OY'
ticker = 'GME'
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={}&apikey={}'.format(ticker, key)
response = requests.get(url)
pprint(response.json())

import asyncio
from alpha_vantage.async_support.timeseries import TimeSeries
symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT', 'GME']
key = 'LAJBI8EN52GC18OY'
async def get_data(symbol):
    ts = TimeSeries(key)
    data, _ = await ts.get_quote_endpoint(symbol)
    await ts.close()
    return data
loop = asyncio.get_event_loop()
tasks = [get_data(symbol) for symbol in symbols]
group1 = asyncio.gather(*tasks)
results = loop.run_until_complete(group1)
pprint(results)
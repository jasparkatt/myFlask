# %%
# this is using the alpha_vantage wrapper python package...not quite the same as using the api directly as code below
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
import matplotlib
import requests
# import json
from pprint import pprint
# Make plots bigger
matplotlib.rcParams['figure.figsize'] = (20.0, 10.0)


# %%
key = 'LAJBI8EN52GC18OY'
ts = TimeSeries(key, output_format='pandas')
ti = TechIndicators(key)

pprint(ts)
pprint(ti)


# %%
aapl_data, aapl_meta_data = ts.get_daily(symbol='GME')
aapl_sma, aapl_meta_sma = ti.get_sma(symbol='GME')
print(aapl_data)
print(aapl_meta_data)
print('      ---break---      ')
pprint(aapl_sma)
print(aapl_meta_sma)


# %%
figure(num=None, figsize=(15, 6), dpi=80, facecolor='w', edgecolor='k')
aapl_data['4. close'].plot()
plt.tight_layout()
plt.grid()
plt.show()

# %%
# this is using the actual api from alphavantage to get the data from the url api


key = 'LAJBI8EN52GC18OY'
ticker = 'GME'
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={}&apikey={}'.format(ticker, key)
response = requests.get(url)
pprint(response.json())

# %%
# messing around with loops to get multi datapoints using alpha_vantage wrapper

key = 'LAJBI8EN52GC18OY'
ts = TimeSeries(key, output_format='pandas')
symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT', 'GME']
for symbol in symbols:
    data = ts.get_daily(symbol)
    pprint(data)


# %%
from alpha_vantage.sectorperformance import SectorPerformances
sp = SectorPerformances(key='LAJBI8EN52GC18OY', output_format='pandas')
data, meta_data = sp.get_sector()
data.describe()

# %%
data['Rank A: Real-Time Performance'].plot(kind='bar')
plt.title('Real Time Performance (%) per Sector')
plt.tight_layout()
plt.grid()
plt.show()

# %%

from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt

key = 'LAJBI8EN52GC18OY'
ts = TimeSeries(key, output_format='pandas')
ti = TechIndicators(key)

aapl_data, aapl_meta_data = ts.get_daily(symbol='AAPL')
aapl_sma, aapl_meta_sma = ti.get_sma(symbol='AAPL')

figure(num=None, figsize=(15, 6), dpi=80, facecolor='w', edgecolor='k')
aapl_data['4. close'].plot()
plt.tight_layout()
plt.grid()
plt.show()

# ts = TimeSeries(key='LAJBI8EN52GC18OY', output_format='pandas')
# data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
# data['close'].plot()
# plt.title('Intraday Times Series for the MSFT stock (1 min)')
# plt.show()

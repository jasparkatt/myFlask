import pandas as pd
import requests
from pprint import pprint

api_key = 'LAJBI8EN52GC18OY'


base_url = 'https://www.alphavantage.co/query?'
params = {'function': 'TIME_SERIES_DAILY_ADJUSTED',
          'symbol': 'GME',
          'apikey': api_key}

response = requests.get(base_url, params=params)
response_dict = response.json()
_, header = response.json()

df = pd.DataFrame.from_dict(response_dict[header], orient='index')

#Clean up column names
df_cols = [i.split(' ')[1] for i in df.columns]
df.columns = df_cols
df.set_index(df.index, inplace=True) #Time-series indexdf.set_index(df.index, inplace=True) #Time-series index

df.set_index(df.index, inplace=True) #Time-series index

pprint(df)
# rename index
print("********************")
df.index.rename('date', inplace=True)
pprint(df)
df.droplevel()
pprint(df)

data2csv = df.to_csv('data2csv.csv', index = True)
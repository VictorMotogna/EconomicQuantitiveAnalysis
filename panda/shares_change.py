import pandas as pd
import matplotlib.pyplot as plt

def read_data_from_file(filename):
  return pd.read_csv(filename)

def set_data_list():
  data = {'INTC': 'Intel',
          'MSFT': 'Microsoft',
          'IBM': 'IBM',
          'BHP': 'BHP',
          'TM': 'Toyota',
          'AAPL': 'Apple',
          'AMZN': 'Amazon',
          'BA': 'Boeing',
          'QCOM': 'Qualcomm',
          'KO': 'Coca-Cola',
          'GOOG': 'Google',
          'SNE': 'Sony',
          'PTR': 'PetroChina'}
  return data

def show_plot():
  plt.show()

ticker = read_data_from_file('ticker_data.csv')
ticker.set_index('Date', inplace=True)

ticker_list = set_data_list()

price_change = pd.Series()

for tick in ticker_list:
    change = 100 * (ticker.loc[ticker.index[-1], tick] - ticker.loc[ticker.index[0], tick]) / ticker.loc[ticker.index[0], tick]
    name = ticker_list[tick]
    price_change[name] = change

price_change.sort_values(inplace=True)
fig, ax = plt.subplots(figsize=(10,8))
price_change.plot(kind='bar', ax=ax)

show_plot()

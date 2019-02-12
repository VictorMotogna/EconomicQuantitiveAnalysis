import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Series example
# s = pd.Series(np.random.randn(4), name='daily returns')
# print(s.describe())

# DataFrame example
df = pd.read_csv('test_pwt.csv')
# print(df)

df = df[['country', 'POP', 'tcgdp']]
df = df.set_index('country')
df.columns = 'population', 'total GDP'
df['population'] = df['population'] * 1e3
df['GDP percap'] = df['total GDP'] * 1e6 / df['population']

df['GDP percap'].plot(kind='bar')
plt.show()
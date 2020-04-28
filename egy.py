import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.ticker as ticker


df = pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv', parse_dates=['Date'])
countries = ['Egypt']
df = df[df['Country'].isin(countries)]
status=['Confirmed', 'Recovered', 'Deaths']
df = df.pivot(index='Date', columns='Country', values=status)
covid = df.reset_index('Date')
covid.set_index(['Date'], inplace=True)

print (covid)

plt.style.use('fivethirtyeight')
plot = covid.plot(figsize=(12,8), linewidth=3, legend=False)
plot.grid(color='#d4d4d4')
plot.set_xlabel('Date')
plot.set_ylabel('Number of Cases in Egypt')
plt.show()

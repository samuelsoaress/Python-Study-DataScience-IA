import pandas as pd
import matplotlib.pylab as plt

base = pd.read_csv('AirPassengers.csv')
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')
base = pd.read_csv('AirPassengers.csv', parse_dates = ['Month'],
                   index_col = 'Month', date_parser = dateparse)
ts = base['#Passengers']

plt.plot(ts)

ts.mean()

ts['1960-01-01':'1960-12-01'].mean()

media_movel = ts.rolling(window = 12).mean()
ts[0:12].mean()
ts[1:13].mean()

plt.plot(ts)
plt.plot(media_movel, color = 'red')

previsoes = []
for i in range(1, 13):
    #print(i)
    superior = len(media_movel) - i
    inferior = superior - 11
    #print(inferior)
    #print(superior)
    #print('---')
    previsoes.append(media_movel[inferior:superior].mean())

previsoes = previsoes[::-1]
plt.plot(previsoes)
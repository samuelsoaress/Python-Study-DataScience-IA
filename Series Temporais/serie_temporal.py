import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from datetime import datetime

base = pd.read_csv('AirPassengers.csv')

print(base.dtypes)

dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m') # Transforma o tipo de data da base pro tipo date
base = pd.read_csv('AirPassengers.csv', parse_dates = ['Month'],
                   index_col = 'Month', date_parser = dateparse) # lendo a base denovo aplicando a função lambda

base.index
ts = base['#Passengers'] # Transforma o dataFrame em uma series

#Fazendo seleções na series{
ts[1]
ts['1949-02']
ts[datetime(1949,2,1)]
ts['1950-01-01':'1950-07-31']
ts[:'1950-07-31']
ts['1950']
#}

ts.index.max() # Trazendo o ultimo registro ou de maior indice
ts.index.min()

plt.plot(ts)

ts_ano = ts.resample('A').sum() #Agrupando por ano e fazendo a soma 
plt.plot(ts_ano) # aqui ele diminuiu a sazionalidade por conta do agrupamento

ts_mes = ts.groupby([lambda x: x.month]).sum()
plt.plot(ts_mes)

ts_datas = ts['1960-01-01':'1960-12-01']
plt.plot(ts_datas)
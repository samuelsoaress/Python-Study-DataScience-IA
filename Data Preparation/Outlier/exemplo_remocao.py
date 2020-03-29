# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 09:02:52 2019

@author: caiqsilv
"""

import pandas as pd

data_pandas = pd.DataFrame([0.1,0.3,5,2,3,4,5,44,6,7,8,99])

data_pandas.sort_values(by=[0])

import matplotlib.pyplot as plt
plt.boxplot(data_pandas.iloc[:,0], showfliers = True)

tamanho = len(data_pandas)

primeiro_quatil = data_pandas.quantile(q=0.25, axis=0, numeric_only=True, interpolation='linear')
terceiro_quartil = data_pandas.quantile(q=0.75, axis=0, numeric_only=True, interpolation='linear')

inicio = round(int(tamanho / primeiro_quatil))
final = int(tamanho - inicio)

linha_inicio = data_pandas.loc[inicio]
linha_final = data_pandas.loc[final]

menor = (int(linha_final - linha_inicio) * 1.5) - inicio
maior = (int(linha_final - linha_inicio) * 1.5) + final

data_pandas[(data_pandas[0] < menor)]
data_pandas[(data_pandas[0] > maior)]

outliers = data_pandas[(data_pandas[0] < menor)]
outliers = data_pandas[(data_pandas[0] > maior)]
    
data_pandas = data_pandas.drop(outliers.index)
    
# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

# IMPORTA O PANDAS E CRIA UM APELIDA PD
import pandas as pd

# CRIA UMA VARIAVEL QUE RECEBE OS DADOS DO ARQUIVO
base = pd.read_csv('credit-data.csv')

# COMANDO PARA DESCREVER OS DADOS
base.describe()

# LOCALIZA TODOS OS DADOS SEM IDADE(AGE)
base.loc[base['age'] < 0]

# APAGAR OS DADOS(NÃO RECOMENDADO)
base.drop('age', 1, inplace = True)

# APAGAR SOMENTE OS REGISTROS COM PROBLEMAS
base.drop(base[base.age < 0].index, inplace = True)

# PREENCHER OS VALORES COM A MEDIA
base.mean()# MEDIA DE TODOS OS CAMPOS
base['age'].mean()# MEDIA DA IDADE
base['age'][base.age > 0].mean()# MEDIA DA IDADE MAIORES QUE 0
base.loc[base.age < 0, 'age'] = 40.92# ATRIBUINDO O VALOR NAS IDADES MENORES QUE 0

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# VERIFICA SE TEM VALORES NULL NA BASE DE DADOS
pd.isnull(base['age'])# 1° FORMA DE VERIFICAR
base.loc[pd.isnull(base['age'])]# 2° FORMA(MELHOR)

# CRIA UMA VARIAVEL PARA RECEBER OS PREVISORES E A CLASSE
previsores = base.iloc[:, 1:4].values# PEGA TODAS AS LINHAS, DA COLUNA 1 ATÉ A 4-1
classe = base.iloc[:, 4].values# PEGA TODAS AS LINHAS, DA COLUNA 4

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)# COLOCA A MEDIA NOS CAMPOS NULOS(NaN)
imputer = imputer.fit(previsores[:, 0:3])
previsores[:, 0:3] = imputer.transform(previsores[:, 0:3])

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#ESCALONAMENTO(PADRONIZAÇÃO DOS DADOS)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)

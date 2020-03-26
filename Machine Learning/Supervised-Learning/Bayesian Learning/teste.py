# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 14:37:36 2019

@author: caiqsilv
"""

import pandas as pd
import numpy as np

base = pd.read_csv('census.csv')

colunas = list()

for row in base:
    colunas.append(row)

for i, colun in enumerate(colunas):
    print(f'{colun}, ', end='')
    
previsores = base.iloc[:, 0:len(colunas) - 1].values
classe = base.iloc[:,len(colunas) - 1].values

from sklearn.preprocessing import LabelEncoder
lambelEncoder_previsores = LabelEncoder()

previsores[:,1] = lambelEncoder_previsores.fit_transform(previsores[:,1])
previsores[:,3] = lambelEncoder_previsores.fit_transform(previsores[:,3])
previsores[:,5] = lambelEncoder_previsores.fit_transform(previsores[:,5])
previsores[:,6] = lambelEncoder_previsores.fit_transform(previsores[:,6])
previsores[:,7] = lambelEncoder_previsores.fit_transform(previsores[:,7])
previsores[:,8] = lambelEncoder_previsores.fit_transform(previsores[:,8])
previsores[:,9] = lambelEncoder_previsores.fit_transform(previsores[:,9])
previsores[:,13] = lambelEncoder_previsores.fit_transform(previsores[:,13])

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy = 'median')# COLOCA A MEDIA NOS CAMPOS NULOS(NaN)
imputer = imputer.fit(previsores[:, 0:len(previsores)])
previsores[:, 0:len(previsores)] = imputer.transform(previsores[:, 0:len(previsores)])

# TRANSFORMA A CLASSE EM BINARIO
labelEnconderClasse = LabelEncoder()
classe = labelEnconderClasse.fit_transform(classe)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#ESCALONAMENTO(PADRONIZAÇÃO DOS DADOS)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)

from sklearn.model_selection import train_test_split
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, classe, test_size=0.25, random_state=0)

## TREINMENTO COM O ALGORITIMO BAYES
#from sklearn.naive_bayes import GaussianNB
#classificador = GaussianNB()
#classificador.fit(previsores_treinamento, classe_treinamento)
#previsoes = classificador.predict(previsores_teste)
#80 PORCENTO DE ACERTO

#from sklearn.tree import DecisionTreeClassifier
#classificador = DecisionTreeClassifier(criterion='entropy', random_state=0)
#classificador.fit(previsores_treinamento, classe_treinamento)
#previsoes = classificador.predict(previsores_teste)
#81 PORCENTO DE ACERTO COM ARVORE DE DECISÃO

#from sklearn.ensemble import RandomForestClassifier
#classificador = RandomForestClassifier(n_estimators=40, criterion='entropy', random_state=0)
#classificador.fit(previsores_treinamento, classe_treinamento)
#previsoes = classificador.predict(previsores_teste)
#85 PORCENTO DE ACERTO COM RANDOM FOREST

from sklearn.neighbors import KNeighborsClassifier
classificador = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p = 2)
classificador.fit(previsores_treinamento, classe_treinamento)
previsoes = classificador.predict(previsores_teste)
#82 PORCENTO DE ACERTO COM KNN

from sklearn.metrics import confusion_matrix, accuracy_score
precisao = accuracy_score(classe_teste, previsoes)
matriz = confusion_matrix(classe_teste, previsoes)

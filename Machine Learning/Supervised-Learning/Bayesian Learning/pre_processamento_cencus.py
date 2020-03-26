# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 10:40:01 2019

@author: caiqsilv
"""

import pandas as pd

base = pd.read_csv('census.csv')

base.describe()

previsores = base.iloc[:, 0:14].values
classe = base.iloc[:,14].values

# SUBSTITUI VALORES STRING PARA NUMEROS
from sklearn.preprocessing import LabelEncoder 
lambelEncoder_previsores = LabelEncoder()
#labels = lambelEncoder_previsores.fit_transform(previsores[:,1])
previsores[:,1] = lambelEncoder_previsores.fit_transform(previsores[:,1])
previsores[:,3] = lambelEncoder_previsores.fit_transform(previsores[:,3])
previsores[:,5] = lambelEncoder_previsores.fit_transform(previsores[:,5])
previsores[:,6] = lambelEncoder_previsores.fit_transform(previsores[:,6])
previsores[:,7] = lambelEncoder_previsores.fit_transform(previsores[:,7])
previsores[:,8] = lambelEncoder_previsores.fit_transform(previsores[:,8])
previsores[:,9] = lambelEncoder_previsores.fit_transform(previsores[:,9])
previsores[:,13] = lambelEncoder_previsores.fit_transform(previsores[:,13])

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# VARIAVEIS DO TIPO DUMMY
from sklearn.preprocessing import OneHotEncoder
#previsores = base.iloc[:, 8:9].values
#previsores[:,0] = lambelEncoder_previsores.fit_transform(previsores[:,0])
oneHotEncoder = OneHotEncoder(categorical_features = [1,3,5,6,7,8,9,13])
previsores = oneHotEncoder.fit_transform(previsores).toarray()

labelEnconderClasse = LabelEncoder()
classe = labelEnconderClasse.fit_transform(classe)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#ESCALONAMENTO(PADRONIZAÇÃO DOS DADOS)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)

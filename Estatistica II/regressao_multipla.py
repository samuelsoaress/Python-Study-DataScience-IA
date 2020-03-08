import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as sm # lib para fazer calculos estatisticos que ja vem por padrão no R 

base = pd.read_csv('mt_cars.csv')
base = base.drop(['Unnamed: 0'], axis = 1)

X = base.iloc[:, 2].values #variavel independente
y = base.iloc[:, 0].values # variavel dependente
correlacao = np.corrcoef(X, y)
X = X.reshape(-1, 1)

modelo = LinearRegression()
modelo.fit(X, y)
modelo.intercept_
modelo.coef_
modelo.score(X, y) #score vai mostrar quanto as colunas independentes explicam a dependentes

previsoes = modelo.predict(X)
modelo_ajustado = sm.ols(formula = 'mpg ~ disp', data = base) # ajustando modelo
modelo_treinado = modelo_ajustado.fit()
modelo_treinado.summary()

plt.scatter(X, y)
plt.plot(X, previsoes, color = 'red')

modelo.predict(200)

X1 = base.iloc[:, 1:4].values # Pegando aqui mais baias
y1 = base.iloc[:, 0].values # pegando a dependente
modelo2 = LinearRegression()
modelo2.fit(X1, y1) 

modelo2.score(X1, y1)
modelo_ajustado2 = sm.ols(formula = 'mpg ~ cyl + disp + hp', data = base)
modelo_treinado2 = modelo_ajustado2.fit()
modelo_treinado2.summary()

novo = np.array([4, 200, 100]) # novo array para passar para o predict na sequecia do modelo
novo = novo.reshape(1, -1) # coloca os atributos em uma coluna
modelo2.predict(novo)


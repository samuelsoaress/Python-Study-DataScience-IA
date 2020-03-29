import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from yellowbrick.regressor import ResidualsPlot # lib pra vizualização de machine Learning

base = pd.read_csv('cars.csv')
base = base.drop(['Unnamed: 0'], axis = 1)

X = base.iloc[:, 1].values # aqui ele transforma no estilo numpy array
X = X.reshape(-1, 1) # transforma as colunas em matriz
y = base.iloc[:, 0].values
correlacao = np.corrcoef(X, y) # aqui é calculado a correlação

modelo = LinearRegression()
modelo.fit(X, y)

modelo.intercept_ # aqui ele mostra a intersecção
modelo.coef_ # aqui o coeficiente

plt.scatter(X, y) # plota um grafico de dispersão
plt.plot(X, modelo.predict(X), color = 'red') # ele desenha a linha da regressão no grafico

# distância 22 pés
modelo.intercept_ + modelo.coef_ * 22 # previsão manual

modelo.predict(22) # aqui o modelo prevê

modelo._residues # mostra a distancia dos dados pra linha de regressão

visualizador = ResidualsPlot(modelo) # plota o grafico de residuos mostrando a dispersão abaixo da intersecção  
visualizador.fit(X, y) 
visualizador.poof() #aqui ele plota o grafico, e quanto mais perto de 0 estiverem os dados mas o modelo está se adequando

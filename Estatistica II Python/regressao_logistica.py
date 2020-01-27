import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression

base = pd.read_csv('Eleicao.csv', sep = ';')
plt.scatter(base.DESPESAS, base.SITUACAO)
base.describe()

np.corrcoef(base.DESPESAS, base.SITUACAO)

X = base.iloc[:, 2].values
X = X[:, np.newaxis]
y = base.iloc[:, 1].values

modelo = LogisticRegression()
modelo.fit(X, y)
modelo.coef_
modelo.intercept_

plt.scatter(X, y)
X_teste = np.linspace(10, 3000, 100)
def model(x):
    return 1 / (1 + np.exp(-x))
r = model(X_teste * modelo.coef_ + modelo.intercept_).ravel()
plt.plot(X_teste, r, color = 'red')

base_previsoes = pd.read_csv('NovosCandidatos.csv', sep = ';')
despesas = base_previsoes.iloc[:, 1].values
despesas = despesas.reshape(-1, 1)
previsoes_teste = modelo.predict(despesas)
base_previsoes = np.column_stack((base_previsoes, previsoes_teste))
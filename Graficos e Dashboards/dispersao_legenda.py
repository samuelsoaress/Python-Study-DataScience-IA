import pandas as pd
import matplotlib.pyplot as plt

base = pd.read_csv('co2.csv')
x = base.conc
y = base.uptake

unicos = list(set(base.Treatment))

for i in range(len(unicos)):
    indice = base.Treatment == unicos[i]
    plt.scatter(x[indice], y[indice], label = unicos[i]) # for com finalidade de pintar os pontos de diferentes categorias
plt.legend(loc = 'lower right') # posiciona a legenda com base nas cores
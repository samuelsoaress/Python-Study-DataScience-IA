# https://github.com/yzhao062/pyod lib python pra detecçãode outlier
import matplotlib.pyplot as plt
import pandas as pd
from pyod.models.knn import KNN

iris = pd.read_csv('iris.csv')

plt.boxplot(iris.iloc[:,1], showfliers = True)# plota sem outlier
plt.boxplot(iris.iloc[:,1]) #plota com outlier
outliers = iris[(iris['sepal width'] > 4.0) | (iris['sepal width'] < 2.1)] # trazendo somente os outliers de acordo com os boxplot

sepal_width = iris.iloc[:,1]
sepal_width = sepal_width.reshape(-1,1) # gerando mais uma coluna pro treino 
detector = KNN()
detector.fit(sepal_width)

previsoes = detector.labels_ # mostra os indices de onde estão os outliers
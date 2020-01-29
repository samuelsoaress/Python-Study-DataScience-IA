import matplotlib.pyplot as plt
import pandas as pd
from pyod.models.knn import KNN

iris = pd.read_csv('iris.csv')

plt.boxplot(iris.iloc[:,1], showfliers = True)
outliers = iris[(iris['sepal width'] > 4.0) | (iris['sepal width'] < 2.1)]

sepal_width = iris.iloc[:,1]
sepal_width = sepal_width.reshape(-1,1)
detector = KNN()
detector.fit(sepal_width)

previsoes = detector.labels_
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

base = pd.read_csv('trees.csv')

plt.hist(base.iloc[:,1], bins = 10)

sns.distplot(base.iloc[:,1], hist = True, kde = True,
             bins = 6, color = 'blue',
             hist_kws={'edgecolor': 'black'}) #kde é a densidade no grafico
                                              # hist se o grafico vai ter histograma
                                              # bins numero de barras 
                                              # hist_kws cor da borda do histograma
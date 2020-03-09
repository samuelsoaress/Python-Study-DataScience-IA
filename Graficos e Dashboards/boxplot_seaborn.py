import pandas as pd
import seaborn as srn

base = pd.read_csv('trees.csv')

srn.boxplot(base.Volume).set_title('Árvores')

srn.boxplot(data = base)
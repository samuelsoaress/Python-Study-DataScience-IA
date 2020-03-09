import pandas as pd
import seaborn as srn
import matplotlib.pyplot as plt

base = pd.read_csv('co2.csv')

srn.scatterplot(base.conc, base.uptake, hue = base.Type)

q = base.loc[base['Type'] == 'Quebec']
m = base.loc[base['Type'] == 'Mississippi']

plt.figure()
plt.subplot(1,2,1)
srn.scatterplot(q.conc, q.uptake).set_title('Quebec')
plt.subplot(1,2,2)
srn.scatterplot(m.conc, m.uptake).set_title('Mississippi')
plt.tight_layout()

# refrigerado e não refrigerado
ch = base.loc[base['Treatment'] == 'chilled']
nc = base.loc[base['Treatment'] == 'nonchilled']

plt.figure()
plt.subplot(1,2,1)
srn.scatterplot(ch.conc, ch.uptake).set_title('Chilled')
plt.subplot(1,2,2)
srn.scatterplot(nc.conc, nc.uptake).set_title('Non chilled')
plt.tight_layout()

base2 = pd.read_csv('esoph.csv')

srn.catplot(x = 'alcgp', y = 'ncontrols', data = base2, jitter = False)

srn.catplot(x = 'alcgp', y = 'ncontrols', data = base2, col = 'tobgp')
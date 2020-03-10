import pandas as pd
import matplotlib.pyplot as plt

base = pd.read_csv('trees.csv')

plt.figure(1)

# girth com volume
plt.subplot(2,2,1)
plt.scatter(base.Girth, base.Volume)

# girth com heigth
plt.subplot(2,2,2) # o terceiro argumento é o id do grafico sendo necessario para subplots
plt.scatter(base.Girth, base.Height)

# heigth com volume
plt.subplot(2,2,3)
plt.scatter(base.Height, base.Volume)

# hsitograma volume
plt.subplot(2,2,4)
plt.hist(base.Volume)
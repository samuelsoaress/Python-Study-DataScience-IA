import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv('IRIS.csv')
iris.head()

iris.shape #mostra quantos dados tem na tabela e colunas
# ex: (150, 5)

iris.describe() #estatistica de todos os dados da sua tabela

iris.isnull().sum() #quantos valores null existem

iris.duplicated().head() # aponta coludas com duplicatas

iris.duplicated().sum() #mostra o total de duplicatas

iris.drop_duplicates(keep=False,inplace=True)# apaga os registros duplicados

plt.figure(figsize = (8, 6))
plt.hist(iris['nome_da_coluna'],
         bins = 20, color = 'g')
plt.xlabel("nome_da_coluna1")
plt.ylabvel("nome_da_coluna2")

#SUBGRAFICOS LADO A LADO 

fig, ax = plt.subplots(1, 2, figsize = (15, 6)) #Grafico de dispersão fora da quaresma
iris.splot(x ="nome_da_coluna", y = "sepal_width",
            kind = "type_grafic", ax = ax[0],
            sharex = False, sharey=False,
            label="apelido", color ="r")

fig, ax = plt.subplots(1, 2, figsize = (15, 6)) #Grafico de dispersão fora da battleland
iris.splot(x ="nome_da_coluna", y = "sepal_width",
            kind = "type_grafic", ax = ax[0],
            sharex = False, sharey=False,
            label="apelido", color ="b")

def plot(species):
    data = iris(iris.species == species) # extrair apenas os registros que estiver dentro desta especie 

    data.plot.scatter('coluna_1', 'coluna_2')

interact(plot) #iteratividade a plotagem 


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score

credito = pd.read_csv('Credit.csv')
previsores = credito.iloc[:,0:20].values
classe = credito.iloc[:,20].values

labelencoder = LabelEncoder()
previsores[:,0] = labelencoder.fit_transform(previsores[:,0])
previsores[:,2] = labelencoder.fit_transform(previsores[:,2])
previsores[:, 3] = labelencoder.fit_transform(previsores[:, 3])
previsores[:, 5] = labelencoder.fit_transform(previsores[:, 5])
previsores[:, 6] = labelencoder.fit_transform(previsores[:, 6])
previsores[:, 8] = labelencoder.fit_transform(previsores[:, 8])
previsores[:, 9] = labelencoder.fit_transform(previsores[:, 9])
previsores[:, 11] = labelencoder.fit_transform(previsores[:, 11])
previsores[:, 13] = labelencoder.fit_transform(previsores[:, 13])
previsores[:, 14] = labelencoder.fit_transform(previsores[:, 14])
previsores[:, 16] = labelencoder.fit_transform(previsores[:, 16])
previsores[:, 18] = labelencoder.fit_transform(previsores[:, 18])
previsores[:, 19] = labelencoder.fit_transform(previsores[:, 19])

X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(previsores,
                                                                  classe,
                                                                  test_size = 0.3,
                                                                  random_state = 0)
naive_bayes = GaussianNB()
naive_bayes.fit(X_treinamento, y_treinamento)

previsoes = naive_bayes.predict(X_teste)
confusao = confusion_matrix(y_teste, previsoes)
taxa_acerto = accuracy_score(y_teste, previsoes)
taxa_erro = 1 - taxa_acerto

from yellowbrick.classifier import ConfusionMatrix
v = ConfusionMatrix(GaussianNB())
v.fit(X_treinamento, y_treinamento)
v.score(X_teste, y_teste)
v.poof()

novo_credito = pd.read_csv('NovoCredit.csv')
novo_credito = novo_credito.iloc[:,0:20].values
novo_credito[:,0] = labelencoder.fit_transform(novo_credito[:,0])
novo_credito[:, 2] = labelencoder.fit_transform(novo_credito[:, 2])
novo_credito[:, 3] = labelencoder.fit_transform(novo_credito[:, 3])
novo_credito[:, 5] = labelencoder.fit_transform(novo_credito[:, 5])
novo_credito[:, 6] = labelencoder.fit_transform(novo_credito[:, 6])
novo_credito[:, 8] = labelencoder.fit_transform(novo_credito[:, 8])
novo_credito[:, 9] = labelencoder.fit_transform(novo_credito[:, 9])
novo_credito[:, 11] = labelencoder.fit_transform(novo_credito[:, 11])
novo_credito[:, 13] = labelencoder.fit_transform(novo_credito[:, 13])
novo_credito[:, 14] = labelencoder.fit_transform(novo_credito[:, 14])
novo_credito[:, 16] = labelencoder.fit_transform(novo_credito[:, 16])
novo_credito[:, 18] = labelencoder.fit_transform(novo_credito[:, 18])
novo_credito[:, 19] = labelencoder.fit_transform(novo_credito[:, 19])

naive_bayes.predict(novo_credito)


import matplotlib.pyplot as plt
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Flatten, Dropout
from keras.utils import np_utils
from keras.layers import Conv2D, MaxPooling2D
from keras.layers.normalization import BatchNormalization

#CARREGANDO A BASE DO KERAS
(X_treinamento, y_treinamento), (X_teste, y_teste) = mnist.load_data()
plt.imshow(X_treinamento[2], cmap = 'gray')
plt.title('Classe ' + str(y_treinamento[0]))

#COLOCANDO OS DADOS NO FORMATO DO TENSORFLOW
previsores_treinamento = X_treinamento.reshape(X_treinamento.shape[0],28, 28, 1)
previsores_teste = X_teste.reshape(X_teste.shape[0], 28, 28, 1)

#TRANSFORMANDO OS DADOS EM FLOAT
previsores_treinamento = previsores_treinamento.astype('float32')
previsores_teste = previsores_teste.astype('float32')

#APLICANDO A NORMALIZAÇÃO PARA QUE FIQUEM ENTRE 0 E 1 NA CAMADA DE ENTRADA
previsores_treinamento /= 255
previsores_teste /= 255

#CRIANDO AS VARIAVEIS DO TIPO DUMMY
classe_treinamento = np_utils.to_categorical(y_treinamento, 10)
classe_teste = np_utils.to_categorical(y_teste, 10)

#CRIANDO O CLASSIFICADOR
classificador = Sequential()

#1° OPERADOR DE CONVOLUÇÃO
#   GERA 32 DETECTORES DE CARACTERISTICAS E 32 MAPAS DE CARACTERISTICAS
#   (3,3) TAMANHO DO KERNELS, DETECTOR DE CARACTERISTICAS
#   STRIDERS IDENTIFICA COMO A JANELA VAI SE MOVER
#   IMPUT_SHAPE INDICA O TAMANHO DA IMAGEM E PADRÃO DE CORES(1 ESCALA DE CINZA, 3 RGB)
#   ACTIVACTION RELU REMOVE NEGATivos para 0
classificador.add(Conv2D(32, (3,3), input_shape=(28, 28, 1), activation = 'relu'))

#APLICANDO A NORMALIZAÇÃO PARA QUE FIQUEM ENTRE 0 E 1 NA CAMADA DE CONVOLUÇÃO(MAPA DE CARACTERISTICAS)
classificador.add(BatchNormalization())

#2° POOLING
#   MAXPOOLING PEGA OS DADOS COM MAIOR VALOR
#   POOL_SIZE TAMANHO DA MATRIZ
classificador.add(MaxPooling2D(pool_size = (2,2)))

#3° FLATTEN
#se tiver mais de uma camada de convolução colocar o flatten no ultimo
#classificador.add(Flatten())

#MELHORIAS NA REDE NEURAL DENSA
#CRIA MAIS UMA CAMADA
classificador.add(Conv2D(32, (3,3), activation = 'relu'))
classificador.add(BatchNormalization())
classificador.add(MaxPooling2D(pool_size = (2,2)))

classificador.add(Flatten())

#4° REDE NEURAL DENSA
#UNITS TAMANHO DOS NEURONIOS
classificador.add(Dense(units = 128, activation = 'relu'))

#ZERA ALGUNS VALORES DE ENTRADA PARA EVITAR OVERFITING
classificador.add(Dropout(0.2))

#CRIA MAIS UMA CAMADA
classificador.add(Dense(units = 128, activation = 'relu'))
classificador.add(Dropout(0.2))

classificador.add(Dense(units = 10, activation = 'softmax'))
classificador.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])

#TREINAMENTO
classificador.fit(previsores_treinamento, classe_treinamento, batch_size = 128, epochs = 5,
                  validation_data = (previsores_teste, classe_teste))

#MOSTRA O RESULTADO DA ACURACIA
resultado = classificador.evaluate(previsores_teste, classe_teste)
resultado

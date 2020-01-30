import numpy as np
from scipy.stats import chi2_contingency

novela = np.array([[19, 6], [43, 32]]) # Criando Array

chi2_contingency(novela) # aqui traz os parametros x-squared[0] e o valor-p[1]
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import ipywidgets as widgets
from ipywidgets import interact, interact_manual

iris = pd.read_csv('IRIS.csv') #Lê o csv 

iris.head()

@interact #adciona interatividade a essa função
def show_articles_more_than(column = 'sepal_length', x=5):
    return iris.loc(iris(column) > x)
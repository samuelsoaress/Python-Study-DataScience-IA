import re
import nltk
nltk.download()

# sem stop, com stop, maior que zero, nltk, add pnltk, função crawler
stop1 = ['é']
stop2 = nltk.corpus.stopwords.words('portuguese')
stop2.append('aa')

splitter = re.compile('\\W+') # \\W caractere não palavra
stemmer = nltk.stem.RSLPStemmer()
lista_palavras = []
lista = [p for p in splitter.split('Este lugar é apavorante python c++ a b c') if p != '']
for p in lista:
    #print(p)
    if stemmer.stem(p).lower() not in stop2:
        if len(p) > 1:
            #print(p)
            lista_palavras.append(stemmer.stem(p.lower()))
            
stemmer.stem('programa')
stemmer.stem('novamente')
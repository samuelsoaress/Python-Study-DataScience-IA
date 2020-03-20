import nltk

stop = nltk.corpus.stopwords.words('portuguese') # aqui pega a lista de strings fora de contexto
stop.append('é') # aqui adicionamos mais uma palavra

def limpa_lançamentos(texto):
    lista = texto.split() # quebra o texto em lista pelos espaços
    lista_palavras = []
    for p in lista:
        if p.lower() not in stop:
            if len(p) > 1:
                lista_palavras.append(p.lower())
    return lista_palavras            
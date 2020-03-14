import urllib3
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
import nltk
import pymysql

def pagina_indexada(url):
    retorno = -1 # não existe a pagina
    conexao = pymysql.connect(host = 'localhost', user='root',passwd='', db='indice')
    cursor_url = conexao.cursor()
    cursor_url.execute('select idurl from urls where url = %s', url)
    if cursor_url.rowcount > 0:
        #print('url já cadastrada')
        idurl = cursor_url.fetchone()[0]
        cursor_palavra = conexao.cursor()
        cursor_palavra.execute('select idurl from palavra_localizacao where idurl = %s',idurl)
        if cursor_palavra.rowcount > 0:
            #print('url com palavras')
            retorno = -2 # existe url com palavras cadastradas  
        else:
            #print('url sem palavras')
            retorno = idurl # existe a pagina sem palavras, retorna o ID da pagina
        cursor_palavra.close()
    cursor_url.close()
    conexao.close()
    
    return retorno

pagina_indexada

def separa_palavras(texto):
    stop = nltk.corpus.stopwords.words('portuguese')
    stemmer = nltk.stem.RSLPStemmer()
    splitter = re.compile('\\W+') 
    lista_palavras = []
    lista = [p for p in splitter.split(texto) if p != '']
    for p in lista:
        if p.lower() not in stop:
            if len(p) > 1:
                lista_palavras.append(stemmer.stem(p).lower())
    return lista_palavras

teste = separa_palavras('este lugar é apavorante')

def get_texto(sopa):
    for tags in sopa(['script','style']):
        tags.decompose()    
    return '  '.join(sopa.stripped_strings)

def crawl(paginas,profundidade):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    novas_paginas = set()
    for i in range(profundidade):
        for pagina in paginas:
            http = urllib3.PoolManager()
            try:
                dados_pagina = http.request('GET',pagina)
            except:
                print('Erro ao abrir a pagina ' + pagina)
                continue
            sopa = BeautifulSoup(dados_pagina.data,'lxml')
            links = sopa.find_all('a')
            contador = 1
            for link in links:
                
                if ('href' in link.attrs):
                    url = urljoin(pagina, str(link.get('href')))
                    
                    if url.find("'") != -1:
                        continue
                    url = url.split('#')[0]
                                    
                    if url[0:4] == 'http':
                        novas_paginas.add(url)
                    contador += 1
        pagina = novas_paginas
    print(contador)
    
lista_paginas = ['https://pt.wikipedia.org/wiki/Linguagem_de_programa%C3%A7%C3%A3o#:~:text=A%20linguagem%20de%20programa%C3%A7%C3%A3o%20%C3%A9,instru%C3%A7%C3%B5es%20de%20processamento%20ao%20computador.']
                 
crawl(lista_paginas,2)    
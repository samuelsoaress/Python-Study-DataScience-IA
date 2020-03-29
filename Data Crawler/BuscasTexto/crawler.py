import urllib3
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
import nltk
import pymysql

def paginaIndexada(url):
    retorno = -1
    conexao = pymysql.connect(host='localhost', user='root', passwd='123456', db='indice')
    cursorUrl = conexao.cursor()
    cursorUrl.execute('select idurl from urls where url = %s', url)
    if cursorUrl.rowcount > 0:
        #print("Url cadastrada")
        idurl = cursorUrl.fetchone()[0]
        cursorPalavra = conexao.cursor()
        cursorPalavra.execute('select idurl from palavra_localizacao where idurl = %s', idurl)
        if cursorPalavra.rowcount > 0:
            #print("Url com palavras")
            retorno = -2
        else:
            #print("Url sem palavras")
            retorno = idurl
        cursorPalavra.close()
    #else:
        #print("Url não cadastrada")
    cursorUrl.close()
    conexao.close()
    
    return retorno

def getIdUrl(url):
    idurl = -1
    conexao = pymysql.connect(host='localhost', user='root', passwd='123456', db='indice', charset="utf8")
    cursor = conexao.cursor()
    cursor.execute('select idurl from urls where url = %s', url)
    if cursor.rowcount > 0:
        idurl = cursor.fetchone()[0]
        
    cursor.close()
    conexao.close()
    return idurl
      
def getIdUrlLigacao(idurl_origem, idurl_destino):
    idurl_ligacao = -1
    conexao = pymysql.connect(host='localhost', user='root', passwd='123456', db='indice')
    cursor = conexao.cursor()
    cursor.execute('select idurl_ligacao from url_ligacao where idurl_origem = %s and idurl_destino = %s', (idurl_origem, idurl_destino))
    if cursor.rowcount > 0:
        idurl_ligacao = cursor.fetchone()[0]
        
    cursor.close()
    conexao.close()
    return idurl_ligacao

#getIdUrlLigacao(399, 400)

def insertPagina(url):
    conexao = pymysql.connect(host='localhost', user='root', passwd='123456', db='indice', autocommit = True, use_unicode=True, charset="utf8mb4")
    cursor = conexao.cursor()
    cursor.execute("insert into urls (url) values (%s)", url)
    idpagina = cursor.lastrowid
    cursor.close()
    conexao.close()
    return idpagina

#insertPagina('teste2')
    
def insertUrlLigacao(idurl_origem, idurl_destino):
    conexao = pymysql.connect(host='localhost', user='root', passwd='123456', db='indice', autocommit = True)
    cursor = conexao.cursor()
    cursor.execute("insert into url_ligacao (idurl_origem, idurl_destino) values (%s, %s)", (idurl_origem, idurl_destino))
    idurl_ligacao = cursor.lastrowid
    cursor.close()
    conexao.close()
    return idurl_ligacao

#insertUrlLigacao(305, 378)
    
def insertUrlPalavra(idpalavra, idurl_ligacao):
    conexao = pymysql.connect(host='localhost', user='root', passwd='123456', db='indice', autocommit = True)
    cursor = conexao.cursor()
    cursor.execute("insert into url_palavra (idpalavra, idurl_ligacao) values (%s, %s)", (idpalavra, idurl_ligacao))
    idurl_palavra = cursor.lastrowid
    cursor.close()
    conexao.close()
    return idurl_palavra

#insertUrlPalavra(244, 1)
    
def palavraIndexada(palavra):
    retorno = -1
    conexao = pymysql.connect(host='localhost', user='root', passwd='123456', db='indice', use_unicode=True, charset="utf8mb4")
    cursor = conexao.cursor()
    cursor.execute('select idpalavra from palavras where palavra = %s', palavra)
    if cursor.rowcount > 0:
        retorno = cursor.fetchone()[0]
    cursor.close()
    conexao.close()
        
    return retorno

#palavraIndexada('Linguagem')

def insertPalavra(palavra):
    conexao = pymysql.connect(host='localhost', user='root', passwd='123456', db='indice', autocommit = True, use_unicode=True, charset="utf8mb4")
    cursor = conexao.cursor()
    cursor.execute("insert into palavras (palavra) values (%s)", palavra)
    idpalavra = cursor.lastrowid
    cursor.close()
    conexao.close()
    return idpalavra

#insertPalavra('teste2')

def insertPalavraLocalizacao(idurl, idpalavra, localizacao):
    conexao = pymysql.connect(host='localhost', user='root', passwd='123456', db='indice', autocommit = True)
    cursor = conexao.cursor()
    cursor.execute("insert into palavra_localizacao (idurl, idpalavra, localizacao) values (%s, %s, %s)", (idurl, idpalavra, localizacao))
    idpalavra_localizacao = cursor.lastrowid
    cursor.close()
    conexao.close()
    return idpalavra_localizacao

#insertPalavraLocalizacao(7, 2, 8)

def indexador(url, sopa):
    indexada = paginaIndexada(url)
    if indexada == -2:
        print("Url já indexada: " + url)
        return
    elif indexada == -1:
        idnova_pagina = insertPagina(url)
    elif indexada > 0:
        idnova_pagina = indexada
    
    print('Indexando: ' + url)
        
    texto = getTexto(sopa)
    palavras = separaPalavras(texto)
    for i in range(len(palavras)):
        palavra = palavras[i]
        idpalavra = palavraIndexada(palavra)
        if idpalavra == -1:
            idpalavra = insertPalavra(palavra)
        insertPalavraLocalizacao(idnova_pagina, idpalavra, i)    
        
def separaPalavras(texto):
    stop = nltk.corpus.stopwords.words('portuguese')
    stemmer = nltk.stem.RSLPStemmer()
    splitter = re.compile('\\W+')
    lista_palavras = []
    lista = [p for p in splitter.split(texto) if p != '']
    for p in lista:
        if stemmer.stem(p.lower()) not in stop:
            if len(p) > 1:
                lista_palavras.append(stemmer.stem(p.lower()))
    return lista_palavras

link = 'https://pt.wikipedia.org/wiki/Linguagem_de_programa%C3%A7%C3%A3o'
link = link.replace('_', ' ')
palavras = separaPalavras(link)

def urlLigaPalavra(url_origem, url_destino):
    texto_url = url_destino.replace('_', ' ')
    palavras = separaPalavras(texto_url)
    idurl_origem = getIdUrl(url_origem)
    idurl_destino = getIdUrl(url_destino)
    if idurl_destino == -1:
        idurl_destino = insertPagina(url_destino)
    
    if idurl_origem == idurl_destino:
        return
    
    if getIdUrlLigacao(idurl_origem, idurl_destino) > 0:
        return
        
    idurl_ligacao = insertUrlLigacao(idurl_origem, idurl_destino)
    for palavra in palavras:
        idpalavra = palavraIndexada(palavra)
        if idpalavra == -1:
            idpalavra = insertPalavra(palavra)
        insertUrlPalavra(idpalavra, idurl_ligacao)

def getTexto(sopa):
    for tags in sopa(['script', 'style']):
        tags.decompose()
    return ' '.join(sopa.stripped_strings)

def crawl(paginas, profundidade):
    contador = 1
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    for i in range(profundidade):
        novas_paginas = set()
    
        # 9 for nas páginas
        for pagina in paginas:
        
            http = urllib3.PoolManager()
            try:
                dados_pagina = http.request('GET', pagina)
            except:
                print('Erro ao abrir a página ' + pagina)
                # 9
                continue
            sopa = BeautifulSoup(dados_pagina.data, "lxml")
            # aqui chama a indexação
            #print('Indexando ' + pagina)
            print(contador)
            contador += 1
            indexador(pagina, sopa)
    
            links = sopa.find_all('a')
            i = 1
            for link in links:
                # 1 mostrar esse primeiro
                #print(str(link.contents) + " - " + str(link.get('href')))
        
                # 2 mostrar os atributos
                #print(link.attrs)
                #print('\n')
        
                # 3 mostrar tópicos vazio
                # 4 criar variável para contar
                # 5 fazer o if pra pegar somente link, com o contador
                if ('href' in link.attrs):
                    # 6 mostrar urljoin com o if, mostrando porque precisa usar ele
                    url = urljoin(pagina, str(link.get('href')))
                    #if url != link.get('href'):
                        #print(url)
                        #print(link.get('href'))
            
                    if url.find("'") != -1:
                        continue
                    # 7 retirar o #
                    #print(url)
                    url = url.split('#')[0]
                    #print(url)
                    #print('\n')
            
                    # 8 adição novas páginas
                    if url[0:4] == 'http':
                        novas_paginas.add(url)
                    urlLigaPalavra(pagina, url)
                     
                
                    i = i + 1
    
            paginas = novas_paginas
        #print(i)
    
           
#a = set() 
#a.add("a") 
#a.add("b")  
#a.add("a")

listapaginas = ['https://pt.wikipedia.org/wiki/Linguagem_de_programa%C3%A7%C3%A3o']    
crawl(listapaginas, 2)



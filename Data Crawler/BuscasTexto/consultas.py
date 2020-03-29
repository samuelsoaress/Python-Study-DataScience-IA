import pymysql
import nltk

def frequencia_score(linhas):
    contagem = dict([linha[0],0] for linha in linhas)
    for linha in linhas:
        contagem[linha[0]] += 1
    return contagem

def localizacao_score(linhas):
    localizacoes = dict([linha[0],1000000] for linha in linhas)
    for linha in linhas:
        soma = sum(linha[1:])
        if soma < localizacoes[linha[0]]:
            localizacoes[linha[0]] = soma
    return soma

def pesquisa(consulta):
    linhas, palavrasid = busca_mais_palavras(consulta)
    #scores = dict([linha[0], 0] for linha in linhas)
    scores = frequencia_score(linhas)
    scoresordenado = sorted([(score,url) for (url, score) in scores.items()], reverse = 0)
    for (score, idurl) in scoresordenado[0:10]:
        print('%f\t%s' % (score,get_url(idurl)))
        

def get_url(idurl):
    retorno = ''
    conexao = pymysql.connect(host = 'localhost', user='root',passwd='', db='indice')
    cursor = conexao.cursor()
    cursor.execute('select url from urls where idurl = %s', idurl)
    if cursor.rowcount > 0:
        retorno = cursor.fetchone()[0]
    cursor.close()
    conexao.close()
    return retorno

    
def busca_mais_palavras(consulta):
    lista_campos = 'p1.idurl'
    lista_tabelas = ''
    lista_clausulas = ''
    palavrasid = []
    palavras = consulta.split(' ')
    numero_tabela = 1
    for palavra in palavras:
        idpalavra = get_idpalavra(palavra)
        if idpalavra > 0:
            palavrasid.append(idpalavra)
            if numero_tabela == 1:
                lista_tabelas += ', '
                lista_clausulas += ' and '
                lista_clausulas += 'p%d.idurl = p%d.idurl and ' % (numero_tabela-1,numero_tabela)
            lista_campos += ', p%d.localizacao' % numero_tabela
            lista_tabelas += ' palavra_localizacao p%d' % numero_tabela
            lista_clausulas += 'p%d.idpalavra = %d' % (numero_tabela, idpalavra)
            numero_tabela += 1
    consulta_completa = 'select %s from %s where %s' % (lista_campos, lista_tabelas, lista_clausulas)
    conexao = pymysql.connect(host = 'localhost', user='root',passwd='', db='indice')
    cursor = conexao.cursor()
    cursor.execute(consulta_completa)
    linhas = [linha for linha in cursor]
    cursor.close()
    conexao.close()
    return linhas,palavrasid

def get_idpalavra(palavra):
    retorno = -1
    stemmer = nltk.stem.RSLPStemmer()
    conexao = pymysql.connect(host = 'localhost', user='root',passwd='', db='indice')
    cursor = conexao.cursor()
    cursor.execute('select idpalavra from palavras where palavra = %s', stemmer.stem(palavra))
    if cursor.rowcount > 0:
        retorno = cursor.fetchone()[0]
    cursor.close()
    conexao.close()
    return retorno

def busca_uma_palava(palavra):
    idpalavra = get_idpalavra(palavra)
    conexao = pymysql.connect(host = 'localhost', user='root',passwd='', db='indice')
    cursor = conexao.cursor()
    cursor.execute('select urls.url from palavra_localizacao plc inner join urls on plc.idurl = urls.idurl where plc.idpalavra = %s',idpalavra)
    paginas = set()
    for url in cursor:
        #print(url[0])
        paginas.add(url[0])
    print('Paginas Encontradas: '+ str(len(paginas)))
    for url in paginas:
        print(url)
    cursor.close()
    conexao.close()

busca_uma_palava('programação')    

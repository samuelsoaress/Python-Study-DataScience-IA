import urllib3
from bs4 import BeautifulSoup

http = urllib3.PoolManager()
pagina = http.request('GET', 'https://pt.wikipedia.org/wiki/Linguagem_de_programa%C3%A7%C3%A3o')

sopa = BeautifulSoup(pagina.data, "lxml")   
for tags in sopa(['script', 'style']):
    tags.decompose() # remove todo o conteúdo da tag
# stripped remove todos os espaços em branco e o join coloca um ao lado do outro ao invés de abaixo
conteudo = ' '.join(sopa.stripped_strings)
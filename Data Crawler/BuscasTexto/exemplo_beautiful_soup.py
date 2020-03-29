# Em 2004, a maioria dos analisadores só conseguiu analisar XML e HTML bem-formados. 
# O material mal formado que você viu na Web foi referido como "tag soup", e apenas um navegador 
# da Web poderia analisá-lo. Beautiful Soup começou como um analisador de HTML que levaria a 
# sopa tag e torná-la linda, ou pelo menos viável.

from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
http = urllib3.PoolManager()
pagina = http.request('GET', 'http://www.iaexpert.com.br')
pagina = http.request('GET', 'https://pt.wikipedia.org/wiki/Linguagem_de_programa%C3%A7%C3%A3o')

# testar sem o lxml para mostrar o warning

sopa = BeautifulSoup(pagina.data, "lxml")
# html.parser

# digitar sopa pra ver o mesmo resultado do urllib3
sopa.title
sopa.title.string
links = sopa.find_all('a')
len(links)
for link in links:
    print(link.get('href'))
    print(link.contents)
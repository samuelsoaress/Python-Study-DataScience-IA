from bs4 import BeautifulSoup
import urllib3

http = urllib3.PoolManager()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

pagina = http.request('GET','http://www.iaexpert.com.br')
pagina2 = http.request('GET','https://pt.wikipedia.org/wiki/Linguagem_de_programa%C3%A7%C3%A3o#:~:text=A%20linguagem%20de%20programa%C3%A7%C3%A3o%20%C3%A9,instru%C3%A7%C3%B5es%20de%20processamento%20ao%20computador.')
                      

pagina.status
pagina2.status

pagina.data

sopa = BeautifulSoup(pagina.data,'lxml')

sopa2 = BeautifulSoup(pagina2.data,'lxml')

sopa

sopa.title

sopa.title.string

links = sopa2.find_all('a')

len(links)

for link in links:
    print(link.get('href'))
    print(link.contents)
import urllib3

# A pool manager is an abstraction for a collection of ConnectionPools.
# If you need to make requests to multiple hosts, then you can use a PoolManager, which takes care of maintaining your pools so you don’t have to.
http = urllib3.PoolManager()
pagina = http.request('GET', 'http://www.iaexpert.com.br')
pagina.status
pagina.data[0:50]
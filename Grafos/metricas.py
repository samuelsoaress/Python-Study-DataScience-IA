from igraph import Graph
from igraph import plot
import igraph

grafo = igraph.load('Grafo.graphml')
print(grafo)

plot(grafo, bbox = (300,300))

grafo.degree(type = 'all')
grafo.degree(type = 'in')
grafo.degree(type = 'out')

grau = grafo.degree(type = 'in')
plot(grafo, vertex_size = grau)

grafo.diameter(directed = True)

grafo.get_diameter()

grafo.neighborhood()

grafo2 = grafo
grafo.isomorphic(grafo2)

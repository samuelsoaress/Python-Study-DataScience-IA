from igraph import Graph
from igraph import plot

grafo = Graph(edges = [(0,2),(0,1),(1,4),(1,5),(2,3),(6,7),(3,7),(4,7),(5,6)],
                       directed = True)
grafo.vs['label'] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
grafo.es['weight'] = [2,1,2,1,2,1,3,1]

plot(grafo, bbox = (300,300), edge_label = grafo.es['weight'])

# A - H
caminho_vertice = grafo.get_shortest_paths(0,7, output = 'vpath')
for n in caminho_vertice[0]:
    #print(n)
    print(grafo.vs[n]['label'])
    
caminho_aresta = grafo.get_shortest_paths(0,7, output = 'epath')

caminho_aresta_id = []
for n in caminho_aresta[0]:
    caminho_aresta_id.append(n)
    
distancia = 0
for e in grafo.es:
    #print(e.index)
    if e.index in caminho_aresta_id:
        distancia += grafo.es[e.index]['weight']
    


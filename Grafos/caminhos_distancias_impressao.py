from igraph import Graph
from igraph import plot

grafo = Graph(edges = [(0,2),(0,1),(1,4),(1,5),(2,3),(6,7),(3,7),(4,7),(5,6)],
                       directed = True)
grafo.vs['label'] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
grafo.es['weight'] = [2,1,2,1,2,1,3,1]

plot(grafo, bbox = (300,300), edge_label = grafo.es['weight'])

# A - H (retorna os vértices)
caminho_vertice = grafo.get_shortest_paths(0,7, output = 'vpath')

# retorna as arestas
caminho_aresta = grafo.get_shortest_paths(0,7, output = 'epath')

caminho_aresta_id = []
for n in caminho_aresta[0]:
    caminho_aresta_id.append(n)
    
caminho_nome_vertices = []
for n in caminho_vertice[0]:
    print(grafo.vs[n]['label'])
    caminho_nome_vertices.append(grafo.vs[n]['label'])
    
for v in grafo.vs:
    #print(v)
    if v['label'] in caminho_nome_vertices:
        v['color'] = 'green'
    else:
        v['color'] = 'gray'
        
for e in grafo.es:
    #print(e)
    if e.index in caminho_aresta_id:
        e['color'] = 'green'
    else:
        e['color'] = 'gray'

    


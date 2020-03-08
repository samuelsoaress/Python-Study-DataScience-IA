from igraph import Graph
from igraph import plot

grafo1 = Graph(edges = [(0,1),(2,2),(2,3),(3,0)], directed = True)
grafo1.vs['label'] = range(grafo1.vcount())
print(grafo1)

grafo2 = Graph(edges = [(0,1),(2,2),(2,3),(3,0)], directed = False)
print(grafo2)

grafo3 = Graph(directed = False)
grafo3.add_vertices(10)
grafo3.add_vertex(16)
grafo3.add_edges([(0,1),(2,2),(2,3),(3,0)])
print(grafo3)
plot(grafo3, bbox=(300,300))

grafo4 = Graph(directed = False)
grafo4.add_vertices(5)
grafo4.add_edges([(0,1),(1,2),(2,3),(3,4),(4,0),(0,2),(2,1)])
grafo4.add_vertex(5)
grafo4.add_vertex(6)
grafo4.vs['label'] = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

plot(grafo4, bbox=(300,300))
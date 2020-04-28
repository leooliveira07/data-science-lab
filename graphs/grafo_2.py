from igraph import Graph
from igraph import plot
# a biblioteca cairo limita a protagem tkplot

grafo1 = Graph(edges = [(0,1), (2,2), (2,3), (3,0)], directed = True)
grafo1.vs['label'] = range(grafo1.vcount())
print(grafo1)

grafo2 = Graph(edges = [(0,1), (2,2), (2,3), (3,0)], directed = False)
print(grafo2)

grafo3 = Graph(directed = False)
grafo3.add_vertices(10)
grafo3.add_vertex(16)
grafo3.add_edges([(0,1), (2,2), (2,3), (3,0)])
plot(grafo3, bbox = (300, 300))

grafo4 = Graph(directed = False)
grafo4.add_vertices(5)
grafo4.add_edges([(0,1), (1,2), (2,3), (3,4), (4,0), (0,2), (2,1)])
grafo4.add_vertex(5)
grafo4.add_vertex(6)

#acrescentando label, porém não está funcionando
grafo4.vs['label'] = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

grafo4.vs['name'] = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

print(grafo4.get_adjacency())
grafo4.get_adjacency()[0,] # Todas as ligações do vértice zero que está na primeira linha
grafo4.get_adjacency()[0,1] # buscar uma adjacência específica

for v in grafo4.vs:
    print(v)

plot(grafo4, bbox = (300, 300))


grafo5 = Graph(edges = [(0,1), (2,3), (0,2), (0,3)], directed = True)
grafo5.vs['label'] = ['Fernando', 'Pedro', 'Jose', 'Antonio']
grafo5.vs['peso'] = [40, 30, 30, 25]

# Visalizar os vértices
for v in grafo5.vs:
    print(v)

grafo5.vs[0] # trazer uma posição específica do vértice do grafo

# Visalizar as arestas
for e in grafo5.es:
    print(e)

grafo5.es['TipoAmizade'] = ['Amigo', 'Inimigo', 'Inimigo', 'Amigo']
grafo5.es['weight'] = [1, 2, 1, 3] # Peso da relação

print(grafo5)

grafo5.vs['type'] = 'Humanos'
grafo5.vs['name'] = 'Amizades'

grafo5.vs['cor'] = ['blue', 'red', 'yellow', 'green']

plot(grafo5, bbox = (300, 300), vertex_size = grafo5.vs['peso'],
     edge_width = grafo5.es['weight'], 
     vertex_color = grafo5.vs['cor'],
     edge_curved = 0.4, vertex_shape = 'square')
# a biblioteca cairo limita a protagem tkplot
# https://ithelp.ithome.com.tw/articles/10274995
# Undirected Graph
# Adjacency Matrix

import numpy as np

vertices = {0, 1, 2, 3, 4}
edges = {(0, 1), (1, 2), (0, 3), (1, 3), (3, 4)}
adjacencyMatrix = np.zeros((5, 5)).astype(int)
for edge in edges:
    v1 = edge[0]
    v2 = edge[1]
    adjacencyMatrix[v1][v2] = 1
    adjacencyMatrix[v2][v1] = 1

print('Vertices', vertices)
print('Edges:', edges)
print(adjacencyMatrix)

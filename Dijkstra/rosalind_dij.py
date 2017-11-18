import collections
import math

def weighted_directed_graph( verticies, edges) :
    verticies = [ v for v in range (1, verticies +1) ]
    d_graph = collections.defaultdict(set)
    weights = collections.defaultdict(int)
    for edge in edges :
        d_graph[edge[0]].add(edge[1])
        weights[(edge[0], edge[1])] = edge[2]
    return [verticies, d_graph, weights]

def dijkstra(vertices, edges, weights):
    q = []
    for vertex in vertices:
        weight = math.inf
        if vertex == 1:
            weight = 0
        q.append((weight, vertex))    
    distances = collections.defaultdict(lambda: -1)
    visited = set()

    while q:
        q.sort(key=lambda x: x[0])  # sort based on the weights
        w, u = q.pop(0)
        if w == math.inf: w = -1
        distances[u] = w    # save v's final distance
        visited.add(u)

        for i in range(len(q)):
            v = q[i]
            if v[1] in edges[u] and v[1] not in visited:   # if the vertices we haven't visited are adjacent to the next vertex
                weight = weights[u, v[1]]
                if w + weight < v[0]:
                    newVertex = (w + weight, v[1]) # tuples are immutable, so create a new tuple to hold the new weight
                    q[i] = newVertex
    return distances



filein = open('rosalind_dij.txt')
data = filein.read()

linesin = [ sublist.strip().split() for sublist in data.splitlines() ]
vertexCount = int(linesin[0][0])
linesin.pop(0)
edges = [(int(edge[0]), int(edge[1]), int(edge[2])) for edge in linesin]
V, E, W = weighted_directed_graph(vertexCount, edges)

distances = dijkstra(V, E, W)

output = [distances[x] for x in sorted(distances.keys())]
print(" ".join(str(x) for x in output))
fileout = open("rosalind_dij_output.txt", "w")
fileout.write(" ".join(str(x) for x in output))
fileout.close()
import collections
import math

def weighted_directed_graph( verticies, edges) :
    verticies = [ v for v in range (1, verticies +1) ]
    d_graph = collections.defaultdict(set)
    weights = collections.defaultdict(int)
    for edge in edges :
        d_graph[ edge[0]].add(edge[1])
        weights[(edge[0], edge[1])] = edge[2]
    return [verticies, d_graph, weights]

def bellman_ford(vertices, edges, weights):
    distances = collections.defaultdict(int)
    for vertex in vertices:
        distances[vertex] = math.inf
    distances[1] = 0
    
    for _ in range(len(vertices)-1):
        for u in edges.keys():
            for v in edges[u]:
                w = weights[(u, v)]
                if distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w
    
    return distances


filein = open('rosalind_bf.txt')
data = filein.read()

linesin = [ sublist.strip().split() for sublist in data.splitlines() ]
vertexCount = int(linesin[0][0])
linesin.pop(0)
edges = [(int(edge[0]), int(edge[1]), int(edge[2])) for edge in linesin]
V, E, W = weighted_directed_graph(vertexCount, edges)

distances = bellman_ford(V, E, W)

output = ""
for v in distances.keys():
    if distances[v] == math.inf:
        output += "x"
    else:
        output += str(distances[v])
    output += " "
print(output)

fileout = open("rosalind_bf_output.txt", "w")
fileout.write(output)
fileout.close()
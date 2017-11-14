import collections
import queue
import math

def weighted_directed_graph( verticies, edges) :
    verticies = [ v for v in range (1, verticies +1) ]
    d_graph = collections.defaultdict(set)
    weights = collections.defaultdict(int)
    for edge in edges :
        d_graph[ edge[0]].add(edge[1])
        weights[(edge[0], edge[1])] = edge[2]
    return [verticies, d_graph, weights]

def dijkstra(vertices, edges, weights):
    q = queue.PriorityQueue()
    for vertex in vertices:
        weight = math.inf
        if vertex == 1:
            weight = 0
        q.put((weight, vertex))
    visited = collections.defaultdict(lambda:False, {})

    while not q.empty():
        w, v = q.get()
        visited[v] = True

        for vertex in edges[v]:
            if not visited[vertex]:
                weight = weights[v, vertex]
                print(weight)



    return -1









filein = open('rosalind_dij.txt')
data = filein.read()

linesin = [ sublist.strip().split() for sublist in data.splitlines() ]
vertexCount = int(linesin[0][0])
linesin.pop(0)
edges = [(int(edge[0]), int(edge[1]), int(edge[2])) for edge in linesin]
V, E, W = weighted_directed_graph(vertexCount, edges)
dijkstra(V, E, W)


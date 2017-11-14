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

def dijkstra(vertices, edges, weights):
    q = []
    for vertex in vertices:
        weight = math.inf
        if vertex == 1:
            weight = 0
        q.append((weight, vertex))    
    distances = collections.defaultdict(lambda: -1)

    while q:
        q.sort(key=lambda x: x[0])  # sort based on the weights
        w, v = q.pop(0)
        if w == math.inf: w = -1
        distances[v] = w #save v's final distance

        # we need to update the weights for the vertices while they are in the queue. queue.PriorityQueue() does not arbitrary access.
        # this method allows access to the weights within the queue without needed an additional structure to track the weights
        for i in range(len(q)):
            vertex = q[i]
            #if the vertices we haven't visited are adjacent to the next vertex
            if vertex[1] in edges[v]:
                weight = weights[v, vertex[1]]
                if w + weight < vertex[0]:
                    newVertex = (w + weight, vertex[1]) #tuples are immutable, so create a new tuple to hold the new weight
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
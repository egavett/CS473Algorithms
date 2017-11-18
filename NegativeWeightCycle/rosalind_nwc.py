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
    
    #check for negative weight cycles 
    for u in edges.keys():
        for v in edges[u]:
            w = weights[(u, v)]
            if distances[u] + w < distances[v]:
                print("Result: 1")
                return "1"    # nwc found: return 1  
    print("Result: -1")
    return "-1"   #no nwc: return -1

filein = open('rosalind_nwc.txt')
graphCount = int(filein.readline())
output = []

for i in range(graphCount):
    print("Begin instance", i)
    nextLine = filein.readline()
    v, e = nextLine.strip().split()
    vertexCount, edgeCount = int(v), int(e)

    data = []
    for _ in range(edgeCount):
        data.append(filein.readline())
    linesin = [ sublist.strip().split() for sublist in data ]
    
    edges = [(int(edge[0]), int(edge[1]), int(edge[2])) for edge in linesin]
    V, E, W = weighted_directed_graph(vertexCount, edges)

    output.append(bellman_ford(V, E, W))

print(" ".join(x for x in output))

fileout = open("rosalind_nwc_output.txt", "w")
fileout.write(" ".join(x for x in output))
fileout.close()
    
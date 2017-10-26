import collections

def undirected_graph( verticies, edges) :
    V = [ v for v in range (1, verticies +1) ]
    und_graph = collections.defaultdict(set)
    for edge in edges :
        und_graph[ edge[0]].add(edge[1])
        und_graph[ edge[1]].add(edge[0])
    return [V, und_graph]

def directed_graph( verticies, edges) :
    V = [ v for v in range (1, verticies +1) ]
    d_graph = collections.defaultdict(set)
    for edge in edges :
        d_graph[ edge[0]].add(edge[1])
    return [V, d_graph]

def BFS(G) :
    depths = collections.defaultdict( lambda:-1, {} )
    vertices, neighbors = G

    def bfs(v) :
        queue = [v]
        depths[v] = 0
        while queue :
            v = queue.pop(0)
            for w in neighbors[v] :
                if depths[w] == -1 :
                    depths[w] = depths[v] + 1
                    queue.append(w)
    bfs(1)
    return depths

def breadth_first_search( vertices, edges ):
    V, E = directed_graph(vertices, edges)
    depths = BFS( (V,E) )
    str_depths = [str(depths[vertex]) for vertex in range(1, vertices+1)]
    return str_depths

filein = open("rosalind_bfs.txt")
data = filein.read()

linesin = [ line.strip().split() for line in data.splitlines() ]
for p in linesin: print(p)
edges = [ [ int(edge[0]), int(edge[1]) ] for edge in linesin ]

filein.close()

output = breadth_first_search(edges[0][0], edges[1:])
print(" ".join(output))
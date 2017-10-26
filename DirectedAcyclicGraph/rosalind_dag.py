import collections

def directed_graph( verticies, edges) :
    V = [ v for v in range (1, verticies +1) ]
    d_graph = collections.defaultdict(set)
    for edge in edges :
        d_graph[ edge[0]].add(edge[1])
    return [V, d_graph]

def DFS(G):
    visited = collections.defaultdict(lambda:False, {})
    vertices, neighbors = G
    stack = []
    is_acyclic = 1

    def dfs(v):
        visited[v] = True
        stack.append(v)
        for w in neighbors[v]:
            if visited[w] == False:
                dfs(w)
            else:
                if w in stack:
                    global is_acyclic
                    is_acyclic = -1
        stack.remove(v)

    for v in vertices:
        if visited[v] == False:
            dfs(v)
    global is_acyclic
    return is_acyclic

def acyclicity_test(vertices, edges):
    V, E = directed_graph(vertices, edges)
    return DFS((V,E))

def start_test(linesin):
    edges = [ [ int(edge[0]), int(edge[1]) ] for edge in linesin ]
    output.append(acyclicity_test(edges[0][0], edges[1:]))
    del edges[:]
    del linesin[:]

filein = open("rosalind_dag.txt")
data = filein.read()[4:]

linesin = []
output = []
for line in data.splitlines():

    if not line.strip():
        start_test(linesin)
    else: 
        linesin.append(line.strip().split())
# algorithm does not detect empty line at the end of the file
start_test(linesin)

print(" ".join(str(x) for x in output))

filein.close()
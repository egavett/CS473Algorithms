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

    def dfs(v):
        visited[v] = True

        for w in neighbors[v]:
            if visited[w] == False:
                dfs(w)
        stack.insert(0, v)

    for v in vertices:
        if visited[v] == False:
            dfs(v)
    return stack

def topological_sort(vertices, edges):
    V, E = directed_graph(vertices, edges)
    sortedVertices = DFS((V,E))
    str_sorted = [str(sortedVertices[vertex]) for vertex in range(0, vertices)]
    return str_sorted

filein = open("rosalind_ts.txt")
data = filein.read()

linesin = [ line.strip().split() for line in data.splitlines() ]
edges = [ [ int(edge[0]), int(edge[1]) ] for edge in linesin ]
filein.close()

output = topological_sort(edges[0][0], edges[1:])
print(" ".join(output))

fileout = open("rosalind_ts_output.txt", "w")
fileout.write(" ".join(str(x) for x in output))
fileout.close()
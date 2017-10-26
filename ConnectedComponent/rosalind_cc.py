import collections

mark = set()

def depth_first_search( graph):
    components = 0
    for vertex in graph.keys():
        if vertex not in mark:
            # new component
            #print("found new component")
            components += 1
            dfs(vertex, graph)
    return components

def dfs(vertex, graph):
    #print("new iteration: {}".format(vertex))
    mark.add(vertex)
    leaves = graph[vertex]
    for leaf in leaves:
        if leaf not in mark:
            dfs(leaf, graph)

def undirected_graph( edges ) :
    und_graph = collections.defaultdict(set)
    for edge in edges :
        und_graph[edge[0]].add(edge[1])
        und_graph[edge[1]].add(edge[0])
    return und_graph



filein = open("rosalind_cc.txt")
data = filein.read()

#note: the following does not add nodes with no connections to the graph
linesin = [ sublist.strip().split() for sublist in data.splitlines() ]

#remove the first line
vertex_count = int(linesin[0][0])
linesin.pop(0)

edges = [ [ int(edge[0]), int(edge[1]) ] for edge in linesin ]
und_graph = undirected_graph( edges )
count = depth_first_search(und_graph)

# account for the missing vertices
print(count + vertex_count - len(und_graph.keys()))
import collections

def undirected_graph( verticies, edges) :
    V = [ v for v in range (1, verticies +1) ]
    und_graph = collections.defaultdict(set)
    for edge in edges :
        und_graph[ edge[0]].add(edge[1])
        und_graph[ edge[1]].add(edge[0])
    return [V, und_graph]

def DFS(G):
    color = 1
    colors = collections.defaultdict(lambda:0, {})
    
    isBicolor = True
    vertices, neighbors = G

    def dfs(v, color):
        colors[v] = color

        for w in neighbors[v]:
            if colors[w] == 0:
                color = colors[v] + 1
                dfs(w, color)
            else:
                if (colors[v]%2) == (colors[w]%2):
                    global isBicolor
                    isBicolor = False
    
    dfs(0, color)
    global isBicolor
    return isBicolor

def bicolor_depth_first( vertices, edges):
    V, E = undirected_graph(vertices, edges)
    isBicolor = DFS((V, E))
    return isBicolor

while int(input()) != 0:
    edgeCount = int(input())
    linesin = []
    for edge in range(0, edgeCount):
        linesin.append( str(input()).strip().split() )

    edges = [ [ int(edge[0]), int(edge[1]) ] for edge in linesin ]

    output = bicolor_depth_first(edges[0][0], edges[0:])
    if output:
        print("BICOLORABLE")
    else:
        print("NOT BICOLORABLE")

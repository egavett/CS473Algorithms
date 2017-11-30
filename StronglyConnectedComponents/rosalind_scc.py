# Implementation of Tarjan's strongly connected components algorithm
# Based off of pseudocode from: https://en.wikipedia.org/wiki/Tarjan's_strongly_connected_components_algorithm

import collections

class Vertex: 
    def __init__(self, value):
        self.value = value
        self.index = -1 # The order in which the vertices are visited; -1 = undefined
        self.lowLink = -1 # -1 = undefined
        self.onStack = False

def directed_graph(verticies, edges) :
    V = collections.defaultdict(Vertex)
    for v in range(1, verticies+1):
        V[v] = Vertex(v)

    d_graph = collections.defaultdict(set)
    for edge in edges :
        d_graph[ edge[0]].add(edge[1])

    return [V, d_graph]

def strongly_connected_component( graph ):
    components = []
    vertices, edges = graph    
    global index
    index = 0
    stack = []

    def SCC(v):
        global index
        vertices[v].index = index
        vertices[v].lowLink = index
        index = index + 1

        stack.append(v)
        vertices[v].onStack = True

        for w in edges[v]:
            if vertices[w].index == -1:
                SCC(w)
                vertices[v].lowLink = min(vertices[v].lowLink, vertices[w].lowLink)
            elif vertices[w].onStack: # deterimine if the vertex is in the current compenent
                vertices[v].lowLink = min(vertices[v].lowLink, vertices[w].index)
        
        if vertices[v].lowLink == vertices[v].index:
            compenent = set()
            w = -1
            while v != w:
                w = stack.pop()
                vertices[w].onStack = False
                compenent.add(w)
            components.append(compenent)

    vertices.keys()
    for v in range(1, len(vertices.keys())+1):
        if vertices[v].index == -1:
            SCC(v)

    return components

filein = open("rosalind_scc.txt")
data = filein.read()
filein.close()

linesin = [sublist.strip().split() for sublist in data.splitlines()]
vertex_count = int(linesin[0][0])
linesin.pop(0) #remove the first line

edges = [[int(edge[0]), int(edge[1])] for edge in linesin]
d_graph = directed_graph(vertex_count, edges)

components = strongly_connected_component(d_graph)

print(len(components))
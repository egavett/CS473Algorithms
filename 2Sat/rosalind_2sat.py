import collections
import sys

class Vertex: 
    def __init__(self, value):
        self.value = value
        self.index = -1 # The order in which the vertices are visited; -1 = undefined
        self.lowLink = -1 # -1 = undefined
        self.onStack = False

def implication_graph(verticies, edges) :
    V = collections.defaultdict(Vertex)
    for v in range(1, verticies+1):
        V[v] = Vertex(v)
        V[-v] = Vertex(-v)

    imp_graph = collections.defaultdict(set)
    for edge in edges:
        imp_graph[-edge[0]].add(edge[1])
        imp_graph[-edge[1]].add(edge[0])
    return [V, imp_graph]

def strongly_connected_component(vertices, edges):
    components = [] 
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
            compenent = []
            w = -1
            while v != w:
                w = stack.pop()
                vertices[w].onStack = False
                compenent.append(w)
            components.append(compenent)

    vertices.keys()
    for v in vertices.keys():
        if vertices[v].index == -1:
            SCC(v)
    
    return components

def two_sat(graph, vertexCount):
    vertices, edges = graph
    components = strongly_connected_component(vertices, edges) # get the stongly connected components of the implication graph

    for component in components:
        vertices = list(component)
        for v in vertices:
            if -v in vertices:      # if a vertex and its implication are in the graph, return 0
                return 0, []      # in an array to match the format of the positive response
    
    # test passed, assign values
    assignments = collections.defaultdict(lambda:None)
    for component in components:
        for vertex in component:
            if assignments[vertex] == None:
                assignments[vertex] = True
                assignments[-vertex] = False

    # form the output
    output = []
    for v in range(1, vertexCount+1):
        if assignments[v]:
            output.append(v)
        else:
            output.append(-v)

    return 1, output

sys.setrecursionlimit(1500)
filein = open("rosalind_2sat.txt")
graphCount = int(filein.readline())
fileout = open("rosalind_2sat_output.txt", "w")

for i in range(graphCount):
    filein.readline()   #skip whitespace
    
    #get data about graph
    nextLine = filein.readline()
    v, e = nextLine.strip().split()
    vertexCount, edgeCount = int(v), int(e)

    # get graph data
    data = []
    for _ in range(edgeCount):
        data.append(filein.readline())
    linesin = [ sublist.strip().split() for sublist in data ]
    edges = [(int(edge[0]), int(edge[1])) for edge in linesin]
    imp_graph = implication_graph(vertexCount, edges)

    result, output = two_sat(imp_graph, vertexCount)
    output_string = "{} {}".format(result, " ".join(str(x) for x in output))
    
    print(output_string)
    fileout.write("{}\n".format(output_string))

filein.close()
fileout.close()
with open('rosalind_ddeg.txt') as text:
    points, lines = [int(x) for x in next(text).split(" ")]
    vertices = [[] for i in range(points)]
    count = 0
    for line in text:
        a, b = [int(x) for x in line.split(" ")]
        vertices[a-1].append(b-1)
        vertices[b-1].append(a-1)
    ddeg = [0] * points
    for connections in vertices:
        for connection in connections:
            ddeg[connection] += len(connections)
    output = ""
    for degree in ddeg:
        output = output + str(degree) + " "
    print output

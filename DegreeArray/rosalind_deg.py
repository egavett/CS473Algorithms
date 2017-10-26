with open('rosalind_deg.txt') as text:
    points, lines = [int(x) for x in next(text).split(" ")] # read first line
    vertices = [0] * points
    for line in text:
        a, b = [int(x) for x in line.split(" ")]
        vertices[a-1] += 1
        vertices[b-1] += 1
    output = ""
    for vertex in vertices:
        output = output + str(vertex) + " "
    print output

import collections

# time complexity: n
# space complexity: n
def two_sum(array): 
    visited = collections.defaultdict(lambda:-1)
    for i in range(len(array)):
        nextValue = array[i]
        if -nextValue in visited.keys():
            return "{} {}".format(visited[-nextValue]+1, i+1)
        else:
            visited[nextValue] = i
    return "-1"

    

filein = open('rosalind_2sum.txt')
data = filein.read()
filein.close()

linesin = [ sublist.strip().split() for sublist in data.splitlines() ]
arrayCount = int(linesin[0][0])

fileout = open("rosalind_2sum_output.txt", "w")

for x in range(1, arrayCount+1):
    array = [int(x) for x in linesin[x]]
    output = two_sum(array)

    print(output)
    fileout.write("{}\n".format(output))

fileout.close()
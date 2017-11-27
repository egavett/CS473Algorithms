import collections

def three_sum(array):
    indices = collections.defaultdict(lambda:-1)    # the problem asks for the original indices, but we need to sort the array
    for i in range(len(array)):                     # the dictionary will allow the retreval of the indices after the n^2 algorith finds three values
        indices[array[i]] = i

    n = len(array)
    array.sort()
    for i in range(0, n-2):
        a = array[i]
        start = i+1
        end = n-1
        while start < end:
            b = array[start]
            c = array[end]
            if a+b+c == 0:
                # return indices
                output = []
                output.append(indices[a]+1)
                output.append(indices[b]+1)
                output.append(indices[c]+1)
                output.sort()
                return " ".join(str(x) for x in output)
            elif a+b+c > 0:
                end = end -1
            else:
                start = start + 1
    return "-1" # no triplet found


filein = open('rosalind_3sum.txt')
data = filein.read()
filein.close()

linesin = [ sublist.strip().split() for sublist in data.splitlines() ]
arrayCount = int(linesin[0][0])

fileout = open("rosalind_3sum_output.txt", "w")

for x in range(1, arrayCount+1):
    array = [int(x) for x in linesin[x]]
    output = three_sum(array)

    print(output)
    fileout.write("{}\n".format(output))

fileout.close()
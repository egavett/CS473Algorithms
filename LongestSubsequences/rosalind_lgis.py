def lgis(array):
    subsequenceLength = []
    reference = []
    bestEnd = 0

    for nextIndex in range(len(array)):
        subsequenceLength.append(1)
        reference.append(None)

        for oldIndex in range(nextIndex):
            length = subsequenceLength[oldIndex]+1
            if array[oldIndex] < array[nextIndex] and length > subsequenceLength[nextIndex]:
                subsequenceLength[nextIndex] = length
                reference[nextIndex] = oldIndex

        if subsequenceLength[nextIndex] > subsequenceLength[bestEnd]:
            bestEnd = nextIndex

    # use the indices to build the actual subsequence
    subsequence = []
    currentReference = bestEnd
    while currentReference is not None:
        subsequence.append(array[currentReference])
        currentReference = reference[currentReference]
    subsequence.reverse()

    return subsequence

def lgds(array):
    subsequenceLength = []
    reference = []
    bestEnd = 0

    for nextIndex in range(len(array)):
        subsequenceLength.append(1)
        reference.append(None)

        for oldIndex in range(nextIndex):
            length = subsequenceLength[oldIndex]+1
            if array[oldIndex] > array[nextIndex] and length > subsequenceLength[nextIndex]:
                subsequenceLength[nextIndex] = length
                reference[nextIndex] = oldIndex

        if subsequenceLength[nextIndex] > subsequenceLength[bestEnd]:
            bestEnd = nextIndex

    # use the indices to build the actual subsequence
    subsequence = []
    currentReference = bestEnd
    while currentReference is not None:
        subsequence.append(array[currentReference])
        currentReference = reference[currentReference]
    subsequence.reverse()

    return subsequence


filein = open("rosalind_lgis.txt")
data = filein.readlines()
filein.close()
inputArray = [int(value) for value in data[1].strip().split()]

fileout = open("rosalind_lgis_output.txt", "w")

output = lgis(inputArray)
print " ".join(str(x) for x in output)
fileout.write(" ".join(str(x) for x in output))

fileout.write("\n")

output = lgds(inputArray)
print " ".join(str(x) for x in output)
fileout.write(" ".join(str(x) for x in output))

fileout.close()
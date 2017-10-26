import collections

def majority_element(array):
    threshold = len(array)/2
    occurrences = collections.defaultdict( lambda:0, {})
    for value in array:
        occurrences[value] +=1
        if occurrences[value] > threshold:
            return value
    return -1

filein = open("rosalind_maj.txt")
data = filein.readlines()[1:]
filein.close()

output = []
for line in data:
    input_array = [int(value) for value in line.strip().split()]
    output.append(majority_element(input_array))
print(" ".join(str(x) for x in output))
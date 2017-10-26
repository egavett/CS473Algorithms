def mergeArrays(array1, array2):
    output = []

    while array1 or array2:
        if not array1:
            output.extend(array2.pop(0) for x in array2)
        elif not array2:
            output.extend(array1.pop(0) for x in array1)
        else:
            if array1[0] < array2[0]:
                output.append(array1.pop(0))
            else:
                output.append(array2.pop(0))
    return output

def mergeSort(array):
    #base case
    if len(array) <= 1:
        return array
    middle = len(array) // 2
    left = mergeSort(array[:middle])
    right = mergeSort(array[middle:])
    return mergeArrays(left, right)

filein = open("rosalind_ms.txt")
data = filein.readlines()
filein.close()
inputArray = [int(value) for value in data[1].strip().split()]

output = mergeSort(inputArray)
print " ".join(str(x) for x in output)

fileout = open("rosalind_ms_output.txt", "w")
fileout.write(" ".join(str(x) for x in output))
fileout.close()
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

filein = open("rosalind_mer.txt")
data = filein.readlines()
filein.close()
array1 = [int(value) for value in data[1].strip().split()]
array2 = [int(value) for value in data[3].strip().split()]
output = mergeArrays(array1, array2)

fileout = open("rosalind_mer_output.txt", "w")

fileout.write(" ".join(str(x) for x in output))

fileout.close()


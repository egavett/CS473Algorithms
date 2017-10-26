import math

def bs_recursive(array, low, high, target):
    if low > high:
        return -1
    middle = (high+low)/2
    if array[middle] == target:
        return middle+1
    elif array[middle] > target:
        return bs(array, low, middle-1, target)
    else:
        return bs(array, middle+1, high, target)

def bs(array, low, high, target):
    while low <= high:
        middle = int(math.floor((low+high)/2))
        if array[middle] == target:
            return middle + 1
        elif target < array[middle]:
            high = middle - 1
        else:
            low = middle + 1
    return -1

def binary_search(array, target):
    return bs(array, 0, len(array)-1, target)

filein = open("rosalind_bins.txt")
data = filein.readlines()
sorted_array = [int(value) for value in data[2].strip().split()]
values = [int(value) for value in data[3].strip().split()]
filein.close()

output = [ binary_search(sorted_array, value) for value in values ]
print(" ".join(str(x) for x in output))

fileout = open("rosalind_bins_output.txt", "w")
fileout.write(" ".join(str(x) for x in output))
fileout.close()
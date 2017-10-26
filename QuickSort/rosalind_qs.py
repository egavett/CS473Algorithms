def partition(array, left, right):
    def swap(i, j):
        temp = array[i]
        array[i] = array[j]
        array[j] = temp

    pivot = array[left]
    i = left + 1
    j = right

    done = False
    while not done:
        while i <= j and array[i] <= pivot:
            i += 1
        while i <= j and array[j] >= pivot:
            j -= 1

        if i > j:
            done = True
        else:
            swap(i,j)
    swap(left,j)
    
    return j
    

def quickSort(array):
    def QS(left, right):
        if left < right:
            s = partition(array, left, right)
            QS(left, s-1)
            QS(s+1, right)

    QS(0, len(array)-1)
    return array



filein = open("rosalind_qs.txt")
data = filein.readlines()
filein.close()
inputArray = [int(value) for value in data[1].strip().split()]

output = quickSort(inputArray)
print " ".join(str(x) for x in output)

fileout = open("rosalind_qs_output.txt", "w")
fileout.write(" ".join(str(x) for x in output))
fileout.close()
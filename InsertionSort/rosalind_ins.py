def insertion_sort( values ):
    swaps = 0
    for i in range(1, len(values)):
        k = i
        while k > 0 and values[k] < values[k-1]:
            temp = values[k]
            values[k] = values[k-1]
            values[k-1] = temp

            k -= 1
            swaps += 1
    return swaps

filein = open("rosalind_ins.txt")
count = int(next(filein))
unsortedArray = [int(x) for x in next(filein).split(" ")]
swaps = insertion_sort(unsortedArray)
print swaps
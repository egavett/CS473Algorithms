
def maxCoins(array):
    maxArray = []
    maxArray.append(0)
    maxArray.append(array[0])
    
    for index in range(2, len(array)):
        print "{}, {}".format(index-1, index-2)
        print maxArray
        print "Comapring {}+{} and {}".format(array[index], maxArray[index-2], maxArray[index-1])
        newMax = max(array[index] + maxArray[index-2], maxArray[index-1])
        print "Chose {}".format(newMax)
        maxArray.append(newMax)
    return maxArray[-1]




numberOfCases = int(input())
for _ in range(numberOfCases):
    ingoreThis = int(input())
    inputStrings = str(raw_input()).strip().split()
    inputArray = [int(x) for x in inputStrings]
    print maxCoins(inputArray)

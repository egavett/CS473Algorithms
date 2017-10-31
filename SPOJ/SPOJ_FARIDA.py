def maxCoins(array):
    maxArray = [0, array[0]]

    for index in range(2, len(array)+1):
        newMax = max(array[index-1] + maxArray[index-2], maxArray[index-1])
        maxArray.append(newMax)
    return maxArray[-1]

numberOfCases = int(input())
for i in range(numberOfCases):
    ingoreThis = int(input()) #parsing works without needed to know the length of the array
    inputStrings = raw_input().strip().split()
    inputArray = [int(x) for x in inputStrings]
    print("Case %d: %d" % (i+1, maxCoins(inputArray)))
import collections

def mortal_fibonacci(months, lifespan):
    dp = collections.defaultdict(lambda: -1, {})
    dp[0], dp[1] = 0, 1
    rabbits = 0
    
    def fibonacci(month):
        if (dp[month] != -1):
            return dp[month]
        else: 
            newRabbits = fibonacci(month-1) + fibonacci(month-2)
            dp[month] = newRabbits
            if month-lifespan >= 0:
                newRabbits -= fibonacci(month-lifespan)
            return newRabbits

    rabbits = fibonacci(months)
    return rabbits



filein = open("rosalind_fibd.txt")
data = filein.read()
filein.close()
m, l = data.split(" ")
months, lifespan = int(m), int(l)

output = mortal_fibonacci(months, lifespan)
print output

fileout = open("rosalind_fibd_output.txt", "w")
fileout.write(str(output))
fileout.close()
a = 4930
b = 9031
total = 0

for x in range(a, b+1):
    if x % 2 == 1:
        total += x
print(total)
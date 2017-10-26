import sys

c = raw_input()
caseCount = int(c)
for case in range(0, caseCount):
    numbers = []
    flag = False
    i = raw_input()
    inputCount = int(i)
    for j in range(0, inputCount):
        v = raw_input()
        value = str(v)
        for number in numbers:
            if number.startswith(value) or value.startswith(number):
                flag = True
        numbers.append(value)
    if flag == False:
        print('NO')
    else:
        print('YES')
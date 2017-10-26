def fibonnaci(count):
    if count == 0 :
        return 0
    elif count == 1 :
        return 1
    else :
        return fibonnaci(count - 1) + fibonnaci(count - 2)

with open('rosalind_fibo.txt') as text:
    for line in text:
        number = int(line)

    print(fibonnaci(number))

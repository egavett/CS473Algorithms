with open('rosalind_ini5.txt') as text:
    for count, line in enumerate(text, 1):
        if count % 2 == 1:
            print(line)

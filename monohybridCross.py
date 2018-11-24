#punnett square with 2 genes
def monopunsquare(a, b, c, d):
    gene1 = a + b
    print("organism 1: " + gene1)
    gene2 = c + d
    print("organism 2: " + gene2)

    print("organism 1 gametes:")
    print(gene1)
    print("organism 2 gametes:")
    print(gene2)

    monochild1 = []
    monochild2 = []
    if a == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I' or 'J' or 'K' or 'L' or 'M' or 'N' or 'O' or 'P' or 'Q' or 'R' or 'S' or 'T' or 'U' or 'V' or 'W' or 'X' or 'Y' or 'Z':
        monochild1.append(a+c)
        monochild1.append(a+d)
        monopun11 = a+c
        monopun12 = a+d

    else:
        monochild1.append(c+a)
        monochild1.append(d+a)
        monopun11 = c+a
        monopun12 = d+a

    #monopun2 time
    if b == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I' or 'J' or 'K' or 'L' or 'M' or 'N' or 'O' or 'P' or 'Q' or 'R' or 'S' or 'T' or 'U' or 'V' or 'W' or 'X' or 'Y' or 'Z':
        monochild2.append(b+c)
        monochild2.append(b+d)
        monopun21 = b+c
        monopun22 = b+d

    else:
        monochild2.append(c+b)
        monochild2.append(c+d)
        monopun21 = c+b
        monopun22 = c+d

    print(monochild1)
    print(monochild2)

    dichild = []
    dichild.append(monochild1+monochild2)

    newset = set([monopun11,monopun12, monopun21, monopun22])
    print("unique combinations:")
    print(newset)

monopunsquare()

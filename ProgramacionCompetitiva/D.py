def Divisor25(num):
    num = num[::-1]
    print(num)
    indice0 = num.find("0")
    indice2 = num.find("2")
    indice5 = num.find("5")
    indice7 = num.find("7")
    print(indice0)
    print(indice5)
    moves = 0
    if (indice0 and indice5) == -1:
        return -1
    if (indice2 and indice5 and indice7) == -1:
        return -1
    if indice0 < indice5:
        num = num[indice0] + num[0:indice0] + num[indice0+1:]
        moves += indice0
    else:
        num = num[indice5] + num[0:indice5] + num[indice5+1:]
        moves += indice5
    print(moves)
    return num

#num = int(input())
num = input()
print(Divisor25(num))


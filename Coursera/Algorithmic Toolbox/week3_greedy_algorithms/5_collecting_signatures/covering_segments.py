
def coveringSegments():
    total = 0
    for i in range(n):
        maxa = a[0]
        actuala = 0
        maxb = b[0]
        actualb = 0
        for i in range(len(a)):
            if a[i] > maxa:
                maxa = a [i]
                actuala = i
            if b[i] > maxb:
                maxb = b[i]
                actualb = i
        total = total + (maxa*maxb)
        a.pop(actuala)
        b.pop(actualb)
    return total


n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
i = [int(x) for x in input().split()]

#print(values)
print(coveringSegments())
    
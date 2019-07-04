def SSD(b,n):
    result = 0
    while n >= 1:
        result += (n%b)**2
        n = int(n/b)
    return result

p = int(input())
for i in range(p):
    numbers = [int(x) for x in input().split()]
    k = numbers[0]
    b = numbers[1]
    n = numbers[2]
    print("%s" % (k), SSD(b,n))
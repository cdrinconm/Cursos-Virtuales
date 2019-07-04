import math
def Divisor(n,k):
    div = []
    print(int(math.sqrt(n)+1))
    for i in range(1,int(math.sqrt(n)+1)):
        print(i)        
        if n % i == 0:
            div.append(i)
    for i in range(len(div)):
        div.append(int(n/div[i]))
    div.append(n)
    print(div)
    if k > len(div):
        return -1
    else:
        return div[k-1]

numbers = [int(x) for x in input().split()]
n = numbers[0]
k = numbers[1]
print(Divisor(n,k))
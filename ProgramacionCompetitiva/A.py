def fibbonaci(k,n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    else:
        array = [0,1]        
        for i in range(n):
            actual = 0
            if len(array) > k:                
                array.pop(0)
            for i in range(len(array)):
                actual += array[i] % 1000000009
            array.append(actual % 1000000009)
    return array[len(array)-1]

numbers = [int(x) for x in input().split()]
k = numbers[0]
n = numbers[1]
while True:
    if n == 0 and k == 0:
        break;
    else:
        print(fibbonaci(k,n))
        numbers = [int(x) for x in input().split()]
        k = numbers[0]
        n = numbers[1]
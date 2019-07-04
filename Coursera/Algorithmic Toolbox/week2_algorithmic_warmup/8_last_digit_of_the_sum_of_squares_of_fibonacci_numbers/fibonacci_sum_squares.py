def fibonacciSquares(num):
    num1 = 0
    num2 = 1
    suma = 0
    total = 1
    if num<=1:
        return num
    for i in range(1,num):
        suma = (num1 + num2) % 10
        num1 = num2
        num2 = suma
    total = (num2*(num1 + num2)) % 10
    return total

n = int(input())
print (fibonacciSquares(n))
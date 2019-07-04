
def fibonacciParcial(start,num):
    num1 = 0
    num2 = 1
    suma = 0
    total = 0
    if num<=1:
        return num
    for i in range(1,num):
        suma = (num1 + num2) % 10
        num1 = num2
        num2 = suma
        #print(num2)        
        if i >= start-1:
            total = (total + num2) % 10
            #print(total)
    return total

number1 = input().split()
n = int(number1[0])
m= int(number1[1])
print (fibonacciParcial(n,m))
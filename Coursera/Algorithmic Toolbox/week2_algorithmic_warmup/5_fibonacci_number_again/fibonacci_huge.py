
def fibonacci(num,mod):
    num1 = 0
    num2 = 1
    suma = 0
    if num<=1:
        return num
    for i in range(num-1):
        suma = (num1 + num2) % mod        
        num1 = num2
        num2 = suma
    return suma

def pisano_period(n):
    if n == 1 or n == 3:
        return n
    if n == 2:
        return 1 
    k = int(n/2)
    if k*2 == n:
        return 4*k
    else:
        return 8*k+4


entrada = input().split()
n = int(entrada[0])
m = int(entrada[1])
print (fibonacci(n % pisano_period(m),m))
"""
entrada = int(input())
print(pisano_period(entrada))
print(2816213588 % 956)
print(fibonacci(108,entrada))
print(pisano_period(25))
"""
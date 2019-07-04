
def fibonacci(n):
	num1 = 0
	num2 = 1
	suma = 0
	if n<=1:
		return n
	for i in range(n-1):
		suma = num1 + num2
		num1 = num2
		num2 = suma
	return suma

entrada = int(input())
print (fibonacci(entrada))

def differentSummands(n,arreglo):
    total = 0
    i = 1
    while total < n:    	
    	if (total + i) == n:
    		arreglo.append(i)
    		return len(arreglo)
    	if (total + i) < n:
    		total = total + i
    		arreglo.append(i)
    	else:
    		arreglo.append(i)
    		total = total + i
    		exc = total - n
    		arreglo.remove(exc)
    		return len(arreglo)
    	i = i + 1

n = int(input())
arreglo = []
result = differentSummands(n,arreglo)
print(result)
for i in range(len(arreglo)):
	print(str(arreglo[i]),end=" ")


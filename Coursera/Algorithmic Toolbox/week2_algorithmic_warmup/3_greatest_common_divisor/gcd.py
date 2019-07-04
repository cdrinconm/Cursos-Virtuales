def mcd(a,b):
	resto = 0
	if b == 0:
		return a
	else:
		resto = a % b
		return mcd(b,resto)

entrada = input().split()
dato = int(entrada[0])
dato2 = int(entrada[1])
print(mcd(dato,dato2))

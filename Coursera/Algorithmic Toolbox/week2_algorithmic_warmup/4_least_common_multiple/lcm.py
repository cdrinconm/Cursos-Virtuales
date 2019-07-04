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
mcd = mcd(dato,dato2)
print(int(dato*dato2/mcd))

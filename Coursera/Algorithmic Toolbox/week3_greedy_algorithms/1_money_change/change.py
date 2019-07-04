
def get_change(m):
    diez = 0
    cinco = 0
    uno = 0
    resto = 0
    #Monedas de 10
    diez = int(m/10)
    resto = int(m%10)
    #Monedas de 5
    cinco = int(resto/5)
    resto = int(resto%5)
    #Monedas de 1
    uno = resto
    return diez + cinco + uno

n = int(input())
print(get_change(n))
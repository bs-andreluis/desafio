def validaNumero(num):
    while num < 1:
        num = int(input('Digite um número válido: '))
    return num

def recPrimo(num, div):
    if div == 1:
        return 1
    if num%div == 0:
        return 0
    return recPrimo(num, div-1)
    

n = validaNumero(int(input('Digite um número: ')))
lista_primos = []

for x in range(2, n+1):
    primo = recPrimo(x, x-1)
    if primo == 1:
        lista_primos.append(x)

print(lista_primos)
    
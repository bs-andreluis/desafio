def validaNumero(num):
    while num < 1:
        num = int(input('Digite um número válido: '))
    return num

n = validaNumero(int(input('Digite um número: ')))
lista_primos = []

for i in range(2, n+1):
    cont = 0;
    for u in range(2, i+1):
        if i%u == 0:
            cont += 1
    if cont == 1:
        lista_primos.append(i)

print(lista_primos)
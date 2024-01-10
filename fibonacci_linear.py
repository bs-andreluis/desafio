def validaNumero(num):
    while num<0:
        num = int(input('Digite um número válido: '))
    return num

sequencia = [0, 1]
n = validaNumero(int(input('Digite quantos termos você deseja: ')))

if n == 0:
    print(sequencia[0])
elif n == 1:
    print(sequencia[1])
else:
    while n-1 >= 1:
        soma = sequencia[-1] + sequencia[-2]
        sequencia.append(soma)
        n -= 1
    print(sequencia[-1])



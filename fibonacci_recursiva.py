def validaNumero(num):
    while num<0:
        num = int(input('Digite um número válido: '))
    return num

def fiboRec(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fiboRec(num - 1) + fiboRec(num - 2)

n = validaNumero(int(input('Digite quantos termos você deseja: ')))
print(fiboRec(n))

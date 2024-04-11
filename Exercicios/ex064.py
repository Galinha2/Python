soma = n = cont = 0

n = int(input('Digite um numero [PARAR = 999]: '))

while n != 999:
    soma += n
    cont += 1

    n = int(input('Digite um numero [PARAR = 999]: '))
    if n == 999:
        print(f'Você digitou {cont} numeros.')
        print(f'A soma de todos os seus valores é: {soma}')
        print('FIM')
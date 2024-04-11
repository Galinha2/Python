soma = cont = p = n = 0
valores = []

while p != 'N':
    n = int(input('Digite um valor: '))
    valores.append(n)

    p = str(input('Quer continuar? [S/N]: ')).upper()
    while p not in 'SN':
        print('Não entendi, digite novamente: ')
        p = str(input('Quer continuar? [S/N]: ')).upper()

    soma += n
    cont += 1

    if p == 'N':
        print(f'Você digitou {cont} numeros.')
        print(f'A média dos numeros digitados é: {soma / cont:.2f}')
        print(f'O numero maior foi o {max(valores)}')
        print(f'O numero menor foi o {min(valores)}')

print('ACABOU')

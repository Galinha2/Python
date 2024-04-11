def leiaint(texto):
    a = str(input(texto))
    while not a.isnumeric():
        print('ERRO, DIGITE UM NUMERO INTEIRO VÁLIDO.')
        a = str(input(texto))
    return int(a)
a = leiaint('Digite um numero: ')
print(f'Você acabou de digitar o numero {a}.')

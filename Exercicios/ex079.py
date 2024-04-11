lista = []

while True:
    valor = (int(input('Digite um valor: ')))
    if valor not in lista:
        lista.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('=-' * 25)
        print('Valor não adicionado.\nNão é possivel adicionar valores repetidos à lista:')
        print('=-' * 25)
    per = str(input('Deseja continuar?[S/N]: ')).upper()
    while per not in 'SN':
        per = str(input('Carater inválido, repita [S/N]: ')).upper()
    if per == 'N':
        break

print('=-' * 20)
print(f'Você digitou os valores {sorted(lista)}')

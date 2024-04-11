n2 = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis',
      'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
      'Quatorze', 'Quinze', 'Dezaseis', 'Dezasete', 'Dezoito',
      'Dezanove', 'Vinte')

while True:
    n = int(input('Digite um numero entre 0 e 20: '))
    while n not in range(0, 21):
        n = int(input('Numero inválido, digite novamente um numero entre 0 e 20: '))
    print(f'O numero {n} enumerado é: {n2[n]}')
    p = str(input('Deseja continuar?[S/N]: ')).upper()
    if p == 'N':
        break
print('Obrigado volte sempre!')

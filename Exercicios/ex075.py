n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))

t = (n1, n2, n3, n4)
print(f'Os valores digitados foram: {t}')
print(f'O valor 9 apareceu {t.count(9)} vezes')
if 3 in t:
    print(f'O valor 3 foi digitado na {t.index(3) + 1}ª posição.')
else:
    print('O valor 3 não foi registrado em nenhuma posição.')
print('Os valores pares são: ', end='')
for c in t:
    if c % 2 == 0:
        print(c, end=' ')

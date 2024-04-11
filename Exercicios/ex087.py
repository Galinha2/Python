lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = ter = 0
for l in range(3):
    for c in range(3):
        lista[l][c] = int(input(f'Digite um valor para {l, c}: '))
        if lista[l][c] % 2 == 0:
            par += lista[l][c]
print('=-'*20)
for l in range(3):
    for c in range(3):
        print(f'[{lista[l][c]:^5}]', end='')
    print()
print('=-'*20)
print(f'A soma dos valores pares é: {par}')
for c in range(3):
    ter += lista[c][2]
print(f'A soma dos valores da terceira coluna é: {ter}')
print(f'O maior valor da segunda linha é: {max(lista[1])}')

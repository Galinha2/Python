valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
print(f'Você digitou os valores: {valores}')
print(f'O maior valor digitado foi {max(valores)} na posição: ', end='')
for p, n in enumerate(valores):
    if n == max(valores):
        print(p, end=' ')
print(f'\nO menor valor digitado foi {min(valores)} na posição: ', end='')
for p, v in enumerate(valores):
    if v == min(valores):
        print(p, end=' ')
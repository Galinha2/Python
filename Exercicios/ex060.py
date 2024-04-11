from math import factorial
n = int(input('Qual numero deseja ver o seu fatorial?: '))
print(f'{n}! = {n}', end=' ')
for c in range(n -1, 0, -1):
    print(('x'), end=' ')
    print(f'{c}', end=' ')
print(f'= {factorial(n)}')

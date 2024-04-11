n = int(input('Digite a constante: '))
r = int(input('Digite a razão: '))
i = 1
while i < 10:
    s = n + r * i
    print(f'{s} -', end=' ')
    i += 1
print('ACABOU')

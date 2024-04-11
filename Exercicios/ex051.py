n = int(input('Digite a constante: '))
r = int(input('Digite a razão: '))
for c in range(1, 10):
    s = n + r * c
    print(s, end=' ')
print('ACABOU')
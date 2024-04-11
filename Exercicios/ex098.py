from time import sleep
def contagem(a, b, p):
    print(f'Contagem de {a} até {b} de {abs(p)} em {abs(p)}')
    for c in range(a, b, p):
        print(c, end=' ')
        sleep(.3)
    print(b, end=' ')
    print('FIM!', end='')
    print()
    print('=-' * 15)

contagem(a = 1, b = 10, p = 1)
contagem(a = 10, b = 0, p = -2)
print('Agora é a sua vez de personalizar a contágem!')
a = int(input('Início: '))
b = int(input('Fim: '))
p = int(input('Passo: '))
if p == 0:
    p = 1
if a > p:
    p = -p
print('=-'*15)
contagem(a, b, p)

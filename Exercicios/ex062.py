n = int(input('Digite a constante: '))
r = int(input('Digite a razão: '))

i = 1
t = 0
s = n + r * i
t2 = 10
tt = 1

while t2 != 0:
    t = t + t2

    while i <= t:
        s = n + r * i

        print(f'{s} -', end=' ')
        i += 1
        tt += 1
    print('PAUSA')

    t2 = int(input('\nQuer adicionar mais quantos termos?: '))

    if t2 == 0:
        print(f'ACABOU com {tt} termos usados.')

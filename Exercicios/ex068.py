print('\033[7m=-\033[m'*14)
print('\033[7mVAMOS JOGAR AO PAR OU IMPAR \033[m')
print('\033[7m=-\033[m'*14)

import random
c = 0

while True:
    n = int(input('Digite um valor: '))
    pi = str(input('Par ou Impar? \033[33m[P/I]\033[m: ')).upper()
    r = random.randint(0, 10)
    s = n + r
    c += 1

    if pi not in ['P', 'I']:
        print('Não entendi, por favor repita')
        pi = str(input('Par ou Impar? \033[33m[P/I]\033[m: ')).upper()

    if s % 2 == 0:
        p = 'PAR'
    else:
        p = 'IMPAR'

    if pi == 'P' and p == 'PAR' or pi == 'I' and p == 'IMPAR':
        print('\033[32mPARABÊNS VOCÊ GANHOU!\033[m')
    elif pi == 'I' and p == 'PAR' or pi == 'P' and p == 'IMPAR':
        print('\033[31mVOCÊ PERDEU!\033[m')
        print(f'Você escolheu: \033[32m{n}\033[m e computador: \033[36m{r}\033[m. Total: \033[33m{s}\033[m = \033[33m{p}\033[m')
        break

    print(f'Você escolheu: \033[32m{n}\033[m e computador: \033[36m{r}\033[m. Total: \033[33m{s}\033[m = \033[33m{p}\033[m')

print(f'\033[31mGAME OVER!!!\033[m Você acabou o jogo com \033[32m{c - 1}\033[m rondas ganhas.')

import random
from time import sleep

print('-='*32)
print('Neste programa você irá tentar adivinhar o numero do computador: ')
print('-='*32)

n1 = int(input('Digite um numero entre 0 e 5: '))
n2 = random.randint(0, 5)

print('Processando', end=''), sleep(.35)
print('.', end=''), sleep(.35)
print('.', end=''), sleep(.35)
print('.'), sleep(.35)

if n1 > 5:
    print(f'{n1} É maior que 5 seu bosta')

if n1 == n2:
    print('Parabêns você acertou!')

else:
    print(f'Você errou')
print(f'A resposta é: {n2}')

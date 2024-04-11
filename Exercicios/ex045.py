import random
from time import sleep

#INTRODUÇÃO
print('\033[7m.:\033[m'*17)
print('\033[7mVAMOS JOGAR PEDRA PAPEL OU TESOURA\033[m')
print('\033[7m.:\033[m'*17)
print()

#ENUNCIADO
print('          \033[4;35mESCOLHA:\033[m')
v = int(input('\033[4;35m1\033[m-\033[1mPEDRA\033[m / \033[4;35m2\033[m-\033[1mPAPEL\033[m / \033[4;35m3\033[m-\033[1mTESOURA\033[m: '))
print('\033[1;30;44m PEDRA ', end=''),  sleep(0.40)
print(' /', end=''), sleep(0.40)
print('  PAPEL ', end=''), sleep(0.40)
print(' /', end=''), sleep(0.40)
print('  TESOURA \033[m '), sleep(0.40)
lista = ['PEDRA', 'PAPEL', 'TESOURA']
r = random.choice(lista)

#ESCOLHAS DA MAQUINA E COMPUTADOR
print('-='*12)
if v == 1:
    print('O \033[32mJOGADOR\033[m jogou: \033[1;33mPEDRA\033[m')
elif v == 2:
    print('O \033[32mJOGADOR\033[m jogou: \033[1;33mPAPEL\033[m')
elif v == 3:
    print('O \033[32mJOGADOR\033[m jogou: \033[1;33mTESOURA\033[m')
print(f'O \033[31mCOMPUTADOR\033[m jogou: \033[1;33m{r}\033[m')
print('=-'*13)

#OPÇÕES E CAUSAS DE JOGO
if v == 1 and r == 'PEDRA':
    print('\033[33mAMBOS EMPATARAM\033[m')
elif v == 1 and r == 'PAPEL':
    print('\033[31mO COMPUTADOR GANHOU\033[m')
elif v == 1 and r == 'TESOURA':
    print('\033[32mO JOGADOR VENCEU\033[m')
elif v == 2 and r == 'PAPEL':
    print('\033[33mAMBOS EMPATARAM\033[m')
elif v == 2 and r == 'PEDRA':
    print('\033[32mO JOGADOR GANHOU\033[m')
elif v == 2 and r == 'TESOURA':
    print('\033[31mO COMPUTADOR GANHOU\033[m')
elif v == 3 and r == 'TESOURA':
    print('\033[33mAMBOS EMPATARAM\033[m')
elif v == 3 and r == 'PEDRA':
    print('\033[31mO COMPUTADOR GANHOU\033[m')
elif v == 3 and r == 'PAPEL':
    print('\033[32mO JOGADOR GANHOU\033[m')
elif v > 3:
    print('\033[31mVocê não digitou nenhuma opção permitida, por favor reinicie o programa!\033[m')

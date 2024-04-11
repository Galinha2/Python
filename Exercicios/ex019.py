print('Sorteio aleatório de qual aluno irá ao quadro')
import random
a1 = input('Digite o seu nome: ')
a2 = input('Digite o seu nome: ')
a3 = input('Digite o seu nome: ')
a4 = input('Digite o seu nome: ')
r = (a1, a2, a3, a4)
print(f'O aluno escolhido foi o {random.choice(r)}')

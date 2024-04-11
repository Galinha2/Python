from random import shuffle
print('Vamos escolher a ordem de inicio de apresentação de cada aluno')
a1 = input('Digite o seu nome: ')
a2 = input('Digite o seu nome: ')
a3 = input('Digite o seu nome: ')
a4 = input('Digite o seu nome: ')
r = [a1, a2, a3, a4]
shuffle(r)
print(f'A ordem de apresentação será: {r}')

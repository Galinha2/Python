from random import randint
def sorteia(a):
    print('Os valores sorteados são:', end=' ')
    for c in range(a):
        a = randint(0, 6)
        while a in lista:
            a = randint(0, 10)
        print(a, end=' ')
        lista.append(a)
    print()
def somapar(b):
    for c in lista:
        if c % 2 == 0:
            par.append(c)
    print(f'Somando os valores pares da lista {lista} temos: {sum(par)}')
lista = []
par = []
sorteia(6)
somapar(0)

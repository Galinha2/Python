import  math
def fatorial(num, show=False):
    '''

    Calcular o fatorial de um numero:

        num: Equivale ao numero introduzido pelo usuário.

        show: Se show=False, mostra apenas o fatorial por inteiro;
              Se show=True, mostra o calculo do fatorial.
    '''
    lista = []
    if show == False:
        for c in range(num, 0, -1):
            lista.append(c)
        s = math.prod(lista)
        print(f'O fatorial de {n} é: {s}')
        print('=-'*20)
    if show == True:
        print('FATORIAL:', end=' ')
        for c in range(num, 0, -1):
            lista.append(c)
            print(c, end=' ')
            if c != 1:
                print('x', end=' ')
        print(f'= {math.prod(lista)}')

n = int(input('Digite um numero para calcular o seu FATORIAL: '))
fatorial(n, show=False)
p = []
while True:
    print('     [1]FATORIAL        [2]FUNÇÃO      ')
    p = int(input('Qual deseja ver?: '))
    if p == 1:
        fatorial(n, show=True)
    elif p == 2:
        help(fatorial)
    print('=-' * 20)

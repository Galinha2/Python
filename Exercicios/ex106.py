#FEITO POR MIM DEPOIS DE VER O VIDEO DE RESOLUÇÃO SOZINHO
from time import sleep
c = ('\033[m',  # 0 - sem cor
     '\033[0;30;41m',  # 1 - vermelho
     '\033[0;30;42m',  # 2 - verde
     '\033[0;30;43m',  # 3 - amarelo
     '\033[0;30;44m',  # 4 - azul
     '\033[0;30;45m',  # 5 - roxo
     '\033[7;97;40m')  # 6 - branco
def comando(com, cor=0):
    sleep(.5)
    print(c[cor], end='')
    help(com)
    print(c[0], end='')
def titulo(tit, cor=0):
    print(c[cor], end='')
    l = len(tit) + 4
    sleep(.5)
    print('~' * l)
    print(f'  {tit}')
    print('~' * l)
    print(c[0], end='')
while True:
    titulo('SISTEMA DE AJUDA PYHELP', 3)
    fun = str(input('Função ou Biblioteca > ')).lower()
    titulo(f'ACESSANDO AO MANUAL DO COMANDO ({fun})', 5)
    comando(fun, 6)

#FEITO POR MIM ANTES DE VER O VIDEO DE RESOLUÇÃO
'''from time import sleep
def ajuda(a):
    while True:
        sleep(1)
        print('\033[;;43m~' * 40)
        print(f'        SISTEMA DE AJUDA PYHELP         ')
        print('~' * 40), print('\033[m')
        f = str(input('\033[mFunção ou Biblioteca > ')).lower().strip()
        if f == 'fim':
            print('\033[;;45mFIM DO PROGRAMA')
            break
        sleep(0.5)
        print('\033[;;46m~'*40)
        print(f'Acessando o Manual do comando ({f})')
        print('~'*40), print('\033[m''\033[7;97;40m')
        sleep(1.5)
        help(f)

ajuda(1)
'''
def menu(titulo):
    print('-'*50)
    print(titulo.center(50))
    print('-' * 50)
def menuIntro(lista):
    menu('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c} -\033[m \033[36m{item}\033[m')
        c += 1

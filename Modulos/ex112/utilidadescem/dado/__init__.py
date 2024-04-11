from Modulos.ex111.utilidadescem import moeda
def leiaDinheiro(per):
    valido = False
    while not valido:
        p = str(input(per)).replace(',','.')
        if p.isalpha() or p.strip() == '':
            print(f'ERRO!! \'{p}\' é um numero inválido.')
        else:
            valido = True
            return float(p)


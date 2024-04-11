def resumo(p, mais, meno):
    print(f'-'*29)
    print('RESUMO DO VALOR'.center(29))
    print(f'-'*29)
    print(f'Preço analisado: {moeda(p):^15}')
    print(f'Dobro do preço: {moeda(p * 2):^18}')
    print(f'Metade do preço: {moeda(p / 2):^15}')
    dez(p, mais)
    menos(p, meno)

def moeda(preço=0):
    return f'{preço:.2f}€'.replace('.',',')

def dez(n, por):
    p = 1 + por / 100
    t = n * p
    print(f'{por}% de aumento: {moeda(t):^17}')

def menos(n, por):
    p = 1 - por / 100
    t = n * p
    print(f'{por}% de aumento: {moeda(t):^17}')

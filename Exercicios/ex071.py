print('BEM VINDO AO BANCO')
d = int(input('Digite o montante que pretende levantar: '))
if d < 10 or d % 2 > 0:
    print('Montante indisponivel, não temos notas inferiores a 10€ ou moedas.')
else:
    nd = [200, 100, 50, 20, 10]

    for n in nd:
        nd = d // n
        if nd > 0:
            print(f'Total de {nd} nota(s) de {n}€')
            d %= n

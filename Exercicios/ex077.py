lista = ('SUSANA', 'HENRIQUE', 'MATILDE', 'LUCAS', 'MAE', 'PAI', 'NUNO')

for c in lista:
    print(f'\nNa palavra {c} temos as vogais: ', end='')
    for vog in c:
        if vog in 'AEIOU':
            print(vog, end=' ')
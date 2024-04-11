def ficha(a, b):
    if a == '':
        a = '<JOGADOR DESCONHECIDO>'
    if b == '':
       b = 0
    print(f'O jogador {a} fez {b} golo(s) no campeonato.')

a = str(input('Digite o nome do jogador: ')).capitalize()
b = str(input('Quantos golos fez o jogador?: '))
ficha(a, b)

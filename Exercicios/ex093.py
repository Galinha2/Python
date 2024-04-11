jogador = {}
jogador['nome'] = str(input('Dijite o seu nome: ')).capitalize()
partidas = int(input(f'Quantas partidas jogou {jogador['nome']}? '))
jogador['golos'] = []
for c in range(partidas):
    golos = int(input(f'Quantos golos fez na {c + 1} partida? '))
    jogador['golos'].append(golos)
jogador['total'] = sum(jogador['golos'])
print('=-'*25)
print(jogador)
print('=-'*25)
for c, k in jogador.items():
    print(f'O campo {c} tem o valor {k}.')
print('=-'*25)
print(f'O jogador {jogador['nome']} jogou {partidas} partidas.')
for c, g in enumerate(jogador['golos']):
    print(f'    => Na partida {c + 1}, fez {g} golos.')
print(f'Foi um total de {jogador['total']} golos!')

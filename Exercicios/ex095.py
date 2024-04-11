lista = []
while True:
    jogador = {}
    jogador['nome'] = str(input('Dijite o seu nome: ')).capitalize()
    partidas = int(input(f'Quantas partidas jogou {jogador['nome']}? '))
    jogador['golos'] = []
    for c in range(partidas):
        golos = int(input(f'Quantos golos fez na {c + 1} partida? '))
        jogador['golos'].append(golos)
    jogador['total'] = sum(jogador['golos'])
    lista.append(jogador)
    per = str(input('Quer continuar?[S/N]: ')).upper()
    while per not in 'SN':
        per = str(input('Não entendi, quer continuar?[S/N]: ')).upper()
    if per == 'N':
        break
print('=-'*25)
print(lista)
print('=-'*25)
print(f'{'Nmº'} {'Nome':<15}{'Golos':<15}{'TOTAL':<20}')
for c in range(len(lista)):
    print(f' {c + 1}  {lista[c]['nome']:<15}{str(lista[c]['golos']):<15}{lista[c]['total']}')
print('-'*50)
while True:
    jog = int(input(f'Introduza um numero entre [1/{len(lista)}] para ver um jogador detalhadamente ou [0] para sair: '))
    if jog > len(lista):
        jog = int(input(f'Numero inválido, introduza APENAS um numero entre [1/{len(lista)}] '
                        f''f'para ver um jogador detalhadamente ou [0] para sair: '))
    if jog == 0:
        break
    gol = lista[jog - 1]
    for c, gols in enumerate(gol['golos']):
        print(f'No jogo {c + 1} fez {gols} golos.')
print('FIM DO PROGRAMA')

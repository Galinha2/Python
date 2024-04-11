print('-='*20)
print('             JOGO DO DADO')
print('-='*20)
from random import randint
from operator import itemgetter
jogador = []
tabela = []
for c in range(4):
    jogadores = {}
    jogadores['Nome'] = str(input('Digite o seu nome: ')).capitalize()
    jogadores['Resultádo'] = randint(1, 6)
    print(f'{jogadores['Nome']} tirou {jogadores['Resultádo']}')
    jogador.append(jogadores)
print('Tabela de Vencedores:')
tabela = sorted(jogador, key=itemgetter('Resultádo'), reverse=True)
for c, l in enumerate(tabela):
    print(f'{c + 1}º lugar: {l['Nome']} com {l['Resultádo']}')

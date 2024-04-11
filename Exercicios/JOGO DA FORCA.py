import random
c = ('\033[m',         # 0 - sem cor
     '\033[0;30;41m',  # 1 - vermelho
     '\033[0;30;42m',  # 2 - verde
     '\033[0;30;43m',  # 3 - amarelo
     '\033[0;30;44m',  # 4 - azul
     '\033[0;30;45m',  # 5 - roxo
     '\033[7;97;40m')  # 6 - branco
def titulo(texto, cor=0):
    l = len(texto) + 4
    print(f'{c[3]}                 ', end=''), print(f'~'*l, end=''), print(f'                   {c[0]}')
    print(f'{c[3]}                 ', end=''), print(f'  {texto}                     {c[0]}')
    print(f'{c[3]}                 ', end=''), print(f'~'*l, end=''), print(f'                   {c[0]}')

tecla = ['Q','W','E','R','T','Y','U','I','O',
         'P','A','S','D','F','G','H','J','K',
         'L','Ç','Z','X','C','V','B','N','M']

palavra = {'Um Animal': ['Macaco', 'Elefante', 'Dinossauro', 'Burro', 'Cão', 'Gato'],
            'Um Objeto': ['Caneta', 'Bolsa', 'Mochila', 'Computador', 'Moeda', 'Telemovel'],
            'Uma Cor': ['Vermelho', 'Verde', 'Branco', 'Preto', 'Azul', 'Roxo', 'Amarelo', 'Majenta']}

pista = random.choice(list(palavra.keys()))
resposta = random.choice(list(palavra[pista]))
acertadas = []

while True:
    titulo('JOGO DO BURRO', cor=3)
    print(f'{c[6]}                Letras Disponiveis:                  {c[0]}')
    for f in tecla:
        print(f'{c[4]}{f}{c[0]}', end=' ')
    print()
    print()
    print(f'                  PISTA: {pista}')
    print(f'{c[2]}{acertadas}{c[0]}')
    print(resposta)
    jogador = input('Digite o seu palpite: ').upper()
    if jogador in resposta:
        tecla.remove(jogador)
        acertadas.append(jogador)
    if len(acertadas) == len(resposta):
        print(f'{c[2]}{acertadas}{c[0]}')
        break

print()
print(f'{c[2]}PARABÊNS ACERTOU!!! A RESPOSTA É: {resposta}{c[0]}')

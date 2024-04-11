from random import randint
jogo = []
print('-'*30)
print('      JOGA NA MEGGA SENA')
print('-'*30)
n = int(input('Quantos jogos você quer que eu sorteie?: '))
print('-=-=-= SORTEANDO 4 JOGOS -=-=-=')

for j in range(n):
    for num in range(6):
        while True:
            r = randint(1, 60)
            if r not in jogo:
                break
        jogo.append(r)
    print(f'Jogo {j +1}: {jogo}')
    jogo.clear()

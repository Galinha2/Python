e = ('Corinthians',	'Palmeiras', 'Santos', 'Grêmio','Cruzeiro',
     'Flamengo', 'Vasco', 'Chapecoense', 'Atlético-MG', 'Botafogo',
     'Atlético-PR', 'Bahia', 'São Paulo','Fluminense', 'Sport',
     'Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

print(f'Lista de equipas do Brasileirão {e[:]}')
print('-'*100)

p = int(input('Quais os primeiros colocados das equipas deseja ver?: '))
print(f'Os {p} primeiros colocados ta tabela foram {e[:p]}')
print('-'*100)

p = int(input('Quais os ultimos colocados das equipas deseja ver?: '))
print(f'Os {p} ultimos colocados ta tabela foram {e[-p:]}')
print('-'*100)

p = int(input('Dijite uma posição entre 1 e 20: '))
print(f'A {p}º posição dirije-se a {e[p - 1]}')
print('-'*100)

print(f'As equipas por ordem alfabética são: {sorted(e)}')
print('-'*100)

galera = []
dado = []
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] > 18:
        print(f'{p[0]} é maior de idade.')
    else:
        print(f'{p[0]} não é maior de idade.')

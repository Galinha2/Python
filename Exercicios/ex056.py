nome = []
idade = []
ih = 0
m = 0
mh = 0
velho = ''
for c in range(1, 5):
    print(f'----{c} PESSOA----')
    n = str(input(f'Nome: '))
    nome.append(n)
    i = int(input(f'Idade: '))
    idade.append(i)
    s = str(input(f'Sexo [M,F]: ')).capitalize()
    if c == 1 and s == 'M':
        mh = i
        velho = n
    if s in 'M' and i > mh:
        mh = i
        velho = n
    if i < 20 and s == 'F':
        m += 1

print(f'A média de idades do grupo é {sum(idade) / 4:.0f}')
print(f'O nome do homem mais velho do grupo é {velho} com {mh} anos.')
print(f'Há {m} mulheres com menos de 20 anos.')
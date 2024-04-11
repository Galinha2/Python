lista = []
for l in range(3):
    for c in range(3):
        n = int(input(f'Digite um valor para {l, c}: '))
        lista.append(n)
print(f'[{lista[0]:^5.0f}]', f'[{lista[1]:^5.0f}]', f'[{lista[2]:^5.0f}]')
print(f'[{lista[3]:^5.0f}]', f'[{lista[4]:^5.0f}]', f'[{lista[5]:^5.0f}]')
print(f'[{lista[6]:^5.0f}]', f'[{lista[7]:^5.0f}]', f'[{lista[8]:^5.0f}]')

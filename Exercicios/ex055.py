p = []

for c in range(1, 7):
    n = float(input('Digite o peso da {}º pessoa: '.format(c)))
    p.append(n)
print(f'O peso menor registrado foi: {min(p)}')
print(f'O peso mair registrado foi: {max(p)}')

s = 0
v = 0
for c in range(1, 7):
    i = int(input('Digite um valor: '))
    if i % 2 == 0:
        s += 1
        v += i
print(f'Escreveu {s} numeros pares')
print(f'A soma dos {s} numeros pares é: {v}')

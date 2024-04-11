s = c = 0
while True:
    n = int(input('Digite um valor (999 para encerar): '))
    if n == 999:
        break
    c += 1
    s += n
print(f'Você digitou {c} valores.')
print(f'A soma dos {c} valores é: {s}')

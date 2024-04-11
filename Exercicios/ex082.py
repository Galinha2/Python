l = []
pa = []
im = []
while True:
    n = (int(input('Digite um valor: ')))
    l.append(n)
    if n % 2 == 0:
        pa.append(n)
    else:
        im.append(n)
    p = str(input('Deseja continuar?[S/N]: ')).upper().strip()
    while p not in 'SN':
        p = str(input('Não entendi. Deseja continuar?[S/N]: ')).upper().strip()
    if p == 'N':
        break

print('-=' * 25)
print(f'A lista completa é: {l}')
print(f'A lista com pares é: {pa}')
print(f'A lista com impares é: {im}')

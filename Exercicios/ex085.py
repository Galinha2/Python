lista = []
impar = []
par = []
for c in range(7):
    n = (int(input(f'Digite o {c+1}º valor: ')))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
lista.append(impar[:])
lista.append(par[:])
print('='*20)
print(f'impar{sorted(lista[0])}')
print(f'par{sorted(lista[1])}')

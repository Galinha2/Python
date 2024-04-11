print('»'*25)
print('   LOJA SUPER BARATÃO')
print('»'*25)
s = mil = c = 0
barato = []
min = float('inf')
while True:
    n = str(input('Nome do Produto: ')).capitalize()
    p = float(input('Preço: R$'))
    per = str(input('Quer continuar?: '))
    c += 1
    s += p
    if p < min:
        min = p
        barato = n
    elif p == min:
        barato.append(n)
    if p > 1000:
        mil += 1
    if per == 'n':
        break
print(f'O total de compras foi R${s}.')
print(f'Temos {mil} produtos custando mais de R$1000.00.')
print(f'O produto com o menor preço é {barato} como o valor de R${min}.')
from Modulos import ex108
n = float(input('Digite o preço: €'))
print(f'A metade de {ex108.valor(n)} é {ex108.dividir(n)}')
print(f'O dobro de {ex108.valor(n)} é {ex108.multiplicar(n)}')
print(f'Aumentando 10% de {ex108.valor(n)} fica {ex108.dez(n, 10)}')
print(f'Reduzindo 13% de {ex108.valor(n)} fica {ex108.menos(n, 13)}')

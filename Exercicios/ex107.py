from Modulos import ex107
n = float(input('Digite o preço: €'))
print(f'A metade de {n} é {ex107.dividir(n)}')
print(f'O dobro de {n} é {ex107.multiplicar(n)}')
print(f'Aumentando 10% de {n} fica {ex107.dez(n, 10)}')
print(f'Reduzindo 13% de {n} fica {ex107.menos(n, 13)}')

from Modulos import ex109
n = float(input('Digite o preço: €'))
print(f'A metade de {ex109.valor(n, True)} é {ex109.dividir(n, True)}')
print(f'O dobro de {ex109.valor(n, True)} é {ex109.multiplicar(n, True)}')
print(f'Aumentando 10% de {ex109.valor(n, True)} fica {ex109.dez(n, 10, False)}')
print(f'Reduzindo 13% de {ex109.valor(n, True)} fica {ex109.menos(n, 13, False)}')

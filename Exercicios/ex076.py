print('-' * 40)
print('           LISTAGEM DE PREÇOS')
print('-' * 40)

lista = ('Lapis', 1.75,
         'Borracha', 2.00,
         'Caderno', 15.90,
         'Estojo', 25.00,
         'Transferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.30,
         'Livro', 34.90)

for c in range(0, len(lista), 2):
    print(f'{lista[c]:.<30} R$ {lista[c + 1]:>7.2f}')

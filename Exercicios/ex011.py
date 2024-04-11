print('Vamos calcular quantos metros quadrados de tinta você necessita para pintar uma parede')
l1 = float(input('Digite quantos metros tem largura: '))
a1 = float(input('Digite quantos metros tem de altura: '))
print(f'Você tem precisamente: {l1*a1:.2f}m² de area para pintar.\nOu seja, necessita de ter pelo menos: {(l1*a1)/2:.2f}L de tinta para a poder pintar.')

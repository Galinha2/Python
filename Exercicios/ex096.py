def terreno(a, b):
    ar = a * b
    print(f'A area do seu terreno de {a:.2f} x {b:.2f} é de {ar:.2f}m2.')


print(' Controlo de Terrenos')
print('----------------------')
l = float(input('LARGURA [m]: '))
c = float(input('COMPRIMENTO [m]: '))
terreno(l, c)

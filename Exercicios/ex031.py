p1 = int(input('Digite a distância da sua viâgem: '))
if p1 <= 200:
    print(f'O bilhete da sua passagem irá custar: $R{p1 * 0.50:.2f}')
else:
    print(f'O bilhete da sua passagem irá custar: $R{p1 * 0.45:.2f}')

print('Aqui você irá saber quanto terá de pagar de acordo com os Km e dias que fêz')
d = int(input('Quantos dias o alugou?: '))
km = float(input('Quantos Km fêz ao todo?: '))
print(f'O valor total que você tem de pagar é: {km*0.15+d*60:.2f}$R')

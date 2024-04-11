print('\033[34m-='*18)
print('\033[33mCALCULADORA DE EMPRÊSTIMO MOBILIÁRIO')
print('\033[34m-='*18)

c = float(input('\033[;30;mDigite o valor da casa: €'))
s = float(input('Digite o valor do seu salário: €'))
a = int(input('Digite quanto anos que tenciona pagar: '))

v = c / a / 12
if c / a / 12 < s * 0.3:
    print(f'Você está autorizado a pedir um emprêstimo no valor de: \033[;31;m{v:.2f}€/mês!')
elif c / a / 12 > s * 0.3:
    print('Você não está autorizado a pagar uma casa')
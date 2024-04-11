s1 = float(input('Digite o valor do seu salário: R$'))
if s1 > 1250:
    print(f'O seu salário irá passar a ser: R${s1 * .10 + s1:.2f}')
else:
    print(f'O seu salário irá passar a ser: R${s1 * .15 + s1:.2f}')

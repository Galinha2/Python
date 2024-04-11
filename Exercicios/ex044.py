p = float(input('Digite o valor do seu produto: '))
print()
print('\033[7mEscolha o seu metodo de PAGAMENTO:\033[m')
print()
print('\033[;36m1\033[m- Dinheiro/Cheque: \033[;33m-10%\033[m')
print('\033[;36m2\033[m- Cartão: \033[;33m-5%\033[m')
print('\033[;36m3\033[m- 2x no Cartão: \033[;33m-0%\033[m')
print('\033[;36m4\033[m- 3x ou mais no Catão: \033[;33m20% Juros\033[m')
v = int(input(''))
if v == 1:
    print(f'O valor \033[1mTOTAL\033[m a pagar é: \033[;32m{p - (p * .1)}€\033[m')
elif v == 2:
    print(f'O valor \033[1mTOTAL\033[m a pagar por é: \033[;32m{(p - (p * .05))}€\033[m')
elif v == 3:
    print(f'O seu valor \033[1mTOTAL\033[m a pagar é: \033[;32m{p / 2}€\033[m por 2 Meses')
elif v == 4:
    i = int(input('Em quantas vezes vai pagar?: '))
    print(f'O seu valor \033[1mTOTAL\033[m a pagar é: \033[;32m{(p + (p * .2)) / i}€\033[m por {i} Meses')

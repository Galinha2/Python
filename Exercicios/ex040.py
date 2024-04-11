n1 = float(input('Digite a nota do seu primeiro teste: '))
n2 = float(input('Digite a sua segunda nota do exame: '))

if (n1 + n2) / 2 > 12:
    print(f'\033[4;32mPARABÊNS!\033[m Você passou de ano, com \033[4;32m{(n1 + n2) / 2:.2f}\033[m valores!!!')
elif (n1 + n2) / 2 < 10:
    print(f' Você foi \033[4;31mREPROVADO!\033[m com média de \033[4;32m{(n1 + n2) / 2:.2f}\033[m valores.')
elif (n1 + n2) / 2 <= 12:
    print(f'Você vai a \033[4;33mRECUPERAÇÃO\033[m com \033[4;32m{(n1 + n2) / 2:.2f}\033[m valores.')

n1 = int(input('Digite um numero inteiro: '))

print('\033[4;34mEscolha uma base de conversão:')
print('\033[0;33m1- \033[4;37mBinário\n\033[0;33m2- \033[4;37mOctal\n\033[0;33m3- \033[4;37mHexadecimal')

n2 = int(input())
if n2 == 1:
    print(bin(n1)[2:])

elif n2 == 2:
    print(oct(n1)[2:])

elif n2 == 3:
    print(hex(n1)[2:])

elif n2 > 3:
    str(input(f'\033[0;30;0mVocê não escolheu nenhuma base da lista, pressione "r" para recomeçar: '))

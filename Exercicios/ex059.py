from time import sleep
v1 = float(input('Digite um valor: '))
v2 = float(input('Digite outro valor: '))
r = 0
while r != 5:
    print('\033[7m:.\033[m' * 11)
    print('[1] - SOMAR\n[2] - MULTIPLICAR\n[3] - MAIOR\n[4] - NOVOS NUMEROS\n[5] - SAIR DO PROGRAMA')
    print('\033[7m:.\033[m' * 11)
    r = int(input(''))
    if r == 1:
        print(f'\033[32mA soma é: \033[32m{v1 + v2:.0f}\033[m')
    elif r == 2:
        print(f'\033[32mA multiplicação é: \033[32m{v1 * v2:.0f}\033[m')
    elif r == 3:
        print(f'\033[32mO numero maior é o {max(v1, v2):.0f}\033[m')
    elif r == 4:
        v1 = float(input('Digite um  novo valor: '))
        v2 = float(input('Digite outro novo valor: '))
    sleep(1)
print(f'\033[32mAté à proxima!!!\033[m')

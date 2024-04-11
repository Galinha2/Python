p = float(input('Digite o seu \033[1;34mPESO\033[m: '))
a = float(input('Digite a sua \033[1;34mALTURA\033[m em metros: '))
imc = p / a**2
if imc < 18.5:
    print(f'O seu IMC é \033[0;36m{imc:.0f}\033[m, você está \033[0;36mABAIXO DO PESO\033[m.')
elif imc < 25:
    print(f'O seu IMC é \033[0;32m{imc:.0f}\033[m, você tem o \033[0;32mPESO IDEAL\033[m.')
elif imc < 30:
    print(f'O seu IMC é \033[0;33m{imc:.0f}\033[m, você tem \033[0;33mSOBREPESO\033[m.')
elif imc < 40:
    print(f'O seu IMC é \033[0;35m{imc:.0f}\033[m, você tem \033[0;35mOBESIDADE\033[m.')
elif imc > 40:
    print(f'O seu imc é \033[0;31m{imc:.0f}\033[m você tem \033[0;31mOBESIDADE MÓRBIDA\033[m.')
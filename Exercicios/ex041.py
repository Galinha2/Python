from datetime import date
a = int(input('Digite o seu ano de nascimento: '))
b = date.today().year
i = b - a
if i <= 9:
    print(f'Você tem \033[0;33m{i} anos\033[m, sua classe é: \033[0;36mMIRIM\033[m')
elif i <= 14:
    print(f'Você tem \033[0;33m{i} anos\033[m, sua classe é: \033[0;36mINFÂNTIL\033[m')
elif i <= 19:
    print(f'Você tem \033[0;33m{i} anos\033[m, sua classe é: \033[0;36mJUNIOR\033[m')
elif i <= 20:
    print(f'Você tem \033[0;33m{i} anos\033[m, sua classe é: \033[0;36mSÊNIOR\033[m')
elif i > 19:
    print(f'Você tem \033[0;33m{i} anos\033[m, sua classe é: \033[0;36mMASTER\033[m')

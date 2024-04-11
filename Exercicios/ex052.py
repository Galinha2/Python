i = int(input('Digite um numero para lhe dizer se é primo ou não: '))
s = 0
for c in range(1, i + 1):
    if i % c == 0:
        s += 1
        print('\033[32m', end=' ')
    else:
        print('\033[m', end=' ')
    print(c, end=' ')
if s > 2:
    print(f'\n\033[m{i} foi divisivel por {s} numeros. \n{i} Não é numero primo')
else:
    print(f'\n{i} foi divisivel por {s} numeros. \n{i} É numero primo')
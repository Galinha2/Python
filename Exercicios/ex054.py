from datetime import date
a = date.today().year
mm = 0
mn = 0
for c in range(1, 7):
    n = int(input(f'Em que ano a {c}º pessoa nasceu?: '))
    s = a - n
    if s < 18:
        mn += 1
        print(f'{n} tem {s} anos, ainda é menor de idade')

    elif s >= 18:
        mm += 1
        print(f'{n} tem {s} anos, já é maior de idade')

print(f'\033[33mTemos aqui {mn} pessoas menores de idade.')
print(f'Temos aqui {mm} pessoas maiores de idade.')

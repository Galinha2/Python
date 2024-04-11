from datetime import date
a = date.today().year
a1 = int(input('Digite um ano ou precione 0 para o ano atual: '))
if a1 == 0:
    a1 = date.today().year
if a1 % 4 == 0:
    print(f'{a1} É um ano bisexto')
else:
    print(f'{a1} Não é um ano bisexto')

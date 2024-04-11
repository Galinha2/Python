from datetime import date
i = int(input('Digite o seu ano de nascimento: '))
a = date.today().year
if a - i < 18:
    print(f'Você tem, {a - i} anos. Faltam ainda \033[4;32m{18 - (a - i)}\033[m anos para se apresentar ao serviço em {(18 - (a - i)) + a}.')
elif a - i == 18:
    print(f'Você tem, {a - i} anos. Tem de se apresentar ao serviço durante este \033[4;32mANO!\033[m de {a}')
elif a > i:
    print(f'Você tem, {a - i} anos. Já passou \033[4;32m{a - i - 18}\033[m anos do seu alistamento em: {a - (a - i - 18)}. ')

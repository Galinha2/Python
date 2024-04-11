maior = mulher = homem = 0
while True:
    print('-' * 25)
    print('   CADRASTE UMA PESSOA')
    print('-' * 25)
    i = int(input('Idade: '))
    if i < 0:
        print('Não entendi, repita por favor.')
        i = int(input('Idade: '))
    s = str(input('Sexo [M/F]: ')).capitalize().strip()
    if s not in ['M', 'F']:
        print('Não entendi, repita por favor.')
        s = str(input('Sexo [M/F]: ')).capitalize().strip()
    print('-' * 20)
    p = str(input('Quer continuar?[S/N]: ')).capitalize().strip()
    if p == 'N':
        break
    elif p not in ['S', 'N']:
        print('Não entendi, repita por favor.')
        p = str(input('Quer continuar?[S/N]: ')).capitalize().strip()
    if i >= 18:
        maior += 1
    if s == 'F' and i <= 20:
        mulher += 1
    if s == 'M':
        homem += 1
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {homem} homens cadastrados.')
print(f'E temos {mulher} mulheres com menos de 20 anos.')

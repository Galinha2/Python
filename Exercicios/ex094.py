lista = []
idades = []
mulheres = []
while True:
    cadastro = {}
    cadastro['nome'] = str(input('Nome: ')).capitalize()
    cadastro['sexo'] = str(input('Sexo[M/F]: ')).upper()
    while cadastro['sexo'] not in 'MF':
        cadastro['sexo'] = str(input('Não entendi, digite apenas o seu Sexo[M/F]: ')).upper()
    if cadastro['sexo'] == 'F':
        mulheres.append(cadastro['nome'])
    cadastro['idade'] = int(input('Idade: '))
    idades.append(cadastro['idade'])
    lista.append(cadastro)
    per = str(input('Quer continuar?[S/N]: ')).upper()
    if per == 'N':
        break
    while per not in 'SN':
        per = str(input('Não entendi, quer continuar?[S/N]: ')).upper()
cadastro['mulheres'] = mulheres[:]
cadastro['idades'] = idades[:]
med = sum(cadastro['idades']) / len(cadastro['idades'])
print('=-'*25)
print(f'    - O grupo tem {len(lista)} pessoas.')
print(f'    - A média de idades é de {med} anos.')
print(f'    - As mulheres cadastradas foram: {cadastro['mulheres']}')
print(f'    - Lista das pessoas que estão a cima da média: ')
for c in range(len(lista)):
    if lista[c]['idade'] > med:
        print(f'        - nome = {lista[c]['nome']}; sexo = {lista[c]['sexo']}; idade = {lista[c]['idade']}')
print('FIM DO PROGRAMA')

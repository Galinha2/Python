dic = {}
dic['Nome'] = str(input('Digite o seu nome: ')).capitalize()
dic['Média'] = float(input(f'Digite a sua média {dic['Nome']}: '))
if dic['Média'] < 10:
    dic['Situação'] = 'reprovado'
else:
    dic['situação'] = 'aprovado'
for k, v in dic.items():
    print(f'{k} é igual a {v}')

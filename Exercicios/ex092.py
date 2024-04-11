from datetime import date
data = date.today().year
dic = {}
dic['Nome'] = str(input('Digite o seu nome: ')).capitalize()
dic['Idade'] = int(input('Ano de nascimento: '))
dic['Idade'] = data - dic['Idade']
dic['Ctps'] = int(input('Carteira de trabalho (0 se não tem): '))
if dic['Ctps'] != 0:
    dic['Contratação'] = int(input('Ano de contratação: '))
    dic['Salário'] = float(input('Seu salário: €'))
    dic['Aposentadoria'] = dic['Contratação'] + 35 - data + dic['Idade']
print('-='*25)
for k, v in dic.items():
    print(f' -{k} tem o valor: {v}')

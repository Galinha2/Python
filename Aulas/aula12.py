n = str(input('Qual é o seu nome?: ')).capitalize()
if n == 'Gustavo':
    print(f'Que nome bonito!')
elif n == 'Pedro' or n == 'Maria' or n == 'Ana' or n == 'Matias':
    print('O seu nome é bastante popular aqui em Portugal!')
elif n in 'Ana Cláudia Jéssica Juliana':
    print('Que belo nome femenino!')
else:
    print(f'Que nome muito vulgar')
print(f'Tenha um bom dia \033[0;33m{n}!')

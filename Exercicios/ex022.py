print('Neste prograna iremos te mostrar algumas funcionalidades do seu nome')
n1 = str(input('Digite o seu nome: ')).strip()
s = n1.split()
r = n1.replace(' ', '')
print(f'Letras maiúsculas: {n1.upper()}')
print(f'Em minúsculas: {n1.lower()}')
print(f'Quantas letras tem no total: {len(r)}')
print(f'Quantas letras tem o primeiro nome: {len(s[0])}')


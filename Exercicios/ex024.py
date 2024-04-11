n1 = str(input('Digite o nome de uma cidade: ')).strip().capitalize()
n2 = n1.split()[0]
n1 = 'Santar' in n2
print(f'Essa cidade começa com o nome "SANTAR"?: {n1}')

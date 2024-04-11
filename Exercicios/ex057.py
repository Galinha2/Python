n = str(input('Digite o seu sexo [M/F]: ')).upper().strip()[0]
while n != 'M' and n != 'F':
    n = str(input('Dados invalidos, informe corretamente o seu sexo: ')).upper().strip()[0]
print(f'Sexo {n} registrado com sucesso!')
print('FIM')

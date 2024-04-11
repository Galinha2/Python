try:
    a = int(input('Valor: '))
    b = int(input('Outro valor: '))
    r = a / b
except Exception as erro:
    print(f'Problema encontrado foi {erro.__class__}')
else:
    print(f'O resultado é {r:.2f}')
finally:
    print('Volte smepre! Muito obrigado!')
 
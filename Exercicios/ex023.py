n1 = int(input('Digite um numero de 0 a 9999: '))
n2 = n1 // 1 % 10
n3 = n1 // 10 % 10
n4 = n1 // 100 % 10
n5 = n1 // 1000 % 10
print(f'O numero {n1} tem:')
print(f'Unidade: {n2:.0f}')
print(f'Dezena: {n3:.0f}')
print(f'Centena: {n4:.0f}')
print(f'Milha: {n5:.0f}')

v1 = int(input('Digite um valor: '))
v2 = int(input('Digite outro valor: '))
if v1 < v2:
    print(f'O valor maior é o: {max(v1, v2)}')
    print(f'O valor menor é o: {min(v1, v2)}')
elif v2 < v1:
    print(f'O valor maior é o: {max(v1, v2)}')
    print(f'O valor menor é o: {min(v1, v2)}')
elif v1 == v2:
    print(f'Ambos os valores {v1} e {v2} são iguais!')
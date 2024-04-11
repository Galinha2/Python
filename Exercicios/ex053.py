n = str(input('Digite uma frase: ')).replace(' ', '').lower()
if n[::-1] == n:
    print(f'{n}é polidromo.')
else:
    print(f'{n} não é polidromo, pois invertido ficaria {n[::-1]}')
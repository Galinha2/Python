def escreva(txt):
    a = len(txt) + 4
    print('~'*a)
    print(f'  {txt}  ')
    print('~'*a)

while True:
    algo = str(input('Escreva algo, ou [0] para PARAR: ')).capitalize()
    if algo == '0':
        break
    escreva(algo)
print('FIM DO PROGRAMA')

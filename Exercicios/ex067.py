while True:
    print('-' * 30)
    n = int(input('Quer ver a tabuada de qual valor?: '))
    print('-' * 30)
    if n < 0:
        break

    for cont in range(0, 11):
        print(n, 'x', cont, '=', n * cont)

print('Obrigado, volte sempre!')

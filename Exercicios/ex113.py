def leiaint(texto):
    while True:
        try:
            a = str(input(texto))
            int(a)
        except (TypeError, ValueError):
            print(f'\033[31mERRO, \'{a}\' não é um numero INTEIRO.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return a

def leiaFloat(texto):
    while True:
        try:
            b = str(input(texto))
            float(b)
        except (ValueError, TypeError):
            print(f'\033[31mERRO, \'{b}\' não é um numero REAL.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return b


a = leiaint('Digite um numero inteiro: ')
b = leiaFloat('Digite um numero real: ')
print(f'O numero inteiro é o {a} e o real o {b}.')

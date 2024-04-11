r1 = float(input('\033[33mDigite a valor de uma reta: '))
r2 = float(input('Digite novamente um valor de uma reta: '))
r3 = float(input('Digite por fim o valor de outra reta: '))
if max(r1, r2, r3) < (r1 + r2 + r3) - max(r1, r2, r3):
    print(f'É possivel criar um triânculo com os seus valores')
else:
    print('Não é possivel criar um triângulo com os seus valores.')
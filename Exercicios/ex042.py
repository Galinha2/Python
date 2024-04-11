n1 = float(input('Digite um valor de uma reta: '))
n2 = float(input('Digite outro valor de uma reta: '))
n3 = float(input('Digite novamente um valor de uma reta: '))

if n1 == n2 == n3:
    print('Você com os seus valores consegue criar um \033[0;36mTriângulo Equilátero\033[0m.')

elif n1 == n2 or n1 == n3 or n2 == n3:
    print('Com os seus valores consegue criar um \033[0;36mTriângulo Isósceles\033[0m.')

elif n1 + n2 > n3 and n2 + n3 > n1 and n3 + n1 > n2:
    print('Com os seus valores consegue fazer um \033[0;36mTriângulo Escaleno\033[0m.')

else:
    print('\033[0;31mNão é possivel criar um Triângulo\033[0m com os seus valores.')
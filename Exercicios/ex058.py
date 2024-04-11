print('\033[7m:.\033[m'*21)
print('\033[7mADIVINHA O NUMERO QUE O COMPUTADOR PENSOU \033[m')
print('\033[7m:.\033[m'*21)
import random
n = int(input('Valor: '))
p = 1
r = random.randint(1, 10)
while n != r:
    if n < r:
        print('\033[33mMaior\033[m -', end=' ')
    if n > r:
        print('\033[36mMenor\033[m -', end=' ')
    n = int(input('\033[31mERROU\033[m, tente novamente: '))
    if n > 10 or n == 0:
        n = int(input('O valor introduzido não existe na base de dados, tente novamente: '))
    p += 1
print(f'\033[32mACERTOU!!!\033[m numero do COMPUTADOR é o: \033[32m{r}\033[m.')
print(f'Precisou de \033[33m{p} palpites para acertar\033[m.')

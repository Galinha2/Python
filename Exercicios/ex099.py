from random import randint
def maior(*num):
        print(num)
        if num == ():
            t = 0
            m = 0
        else:
            t = len(num)
            m = max(num)
        print(f'Foram informados {t} valores ao todo.')
        print(f'O maior valor informado foi {m}.')
        print('=-'* 20)
maior(6,8,2,1,7,10)
maior(7,4,3)
maior(8,3)
maior(5)
maior()

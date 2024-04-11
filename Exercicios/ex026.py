f1 = str(input('Diga uma frase: ')).strip().upper().replace(' ', '')
en = str(input('Qual letra pretende encontrar?: ')).upper()
f2 = f1.count(f'{en}')
f3 = f1.find(f'{en}')+1
f4 = (f1.rfind(f'{en}')+1)
print(f'Na frase {f1}, aparece: ')
print(f'{f2}x a letra "{en}".')
print(f'A primeira vez na: {f3}º posição. ')
print(f'E pela ultima vez na: {f4}º posição. ')

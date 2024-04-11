e = str(input('Digite uma expressão: '))
dir = list()
esq = list()
for simb in e:
    if simb == '(':
        dir.append(1)
    elif simb == ')':
        esq.append(1)
if len(dir) == len(esq):
    print('correta')
else:
    print('incorreta')

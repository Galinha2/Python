l = []
while True:
    n = int(input('Digite um valor: '))
    l.append(n)
    p = str(input('Deseja continuar?[S/N]: ')).upper().strip()
    while p not in 'SN':
        p = str(input('Não entendi. Deseja continuar?[S/N]: ')).upper().strip()
    if p == 'N':
        break
l.sort(reverse=True)
print('-='*25)
print(f'Você digitou {len(l)} elementos')
print(f'A ordem decrescente é: {l}')
if 5 in l:
    print(f'O valor 5 faz parte na lista! na posição {l.index(5)}')
else:
    print('O valor 5 não faz parte na lista!')

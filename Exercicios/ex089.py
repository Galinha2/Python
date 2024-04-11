lista = []
while True:
    nomes = str(input('Digite o seu nome: ')).capitalize()
    notas = []
    for c in range(2):
        nota = float(input(f'Digite a {c + 1}º nota: '))
        notas.append(nota)
    med = [(sum(notas)) / 2]
    lista.append([nomes, notas, med])
    per = str(input('Quer continuar?[S/N]: ')).upper().strip()
    while per not in 'SN':
        per = str(input('Não entendi, quer continuar?[S/N]: ')).upper()
    if per == 'N':
        break
print('-='*35)
print('No.  NOME      NOTAS       MÉDIA')
print('-'*40)
for i, aluno in enumerate(lista, start=1):
    print(f'.{i:<3}{aluno[0]:<8}{aluno[1][0]:<5}/ {aluno[1][1]:<8}{aluno[2][0]:<20}')
print('-'*35)
while True:
    m = int(input('Quer ver a nota individual de algum aluno? Introduza o seu numero[ou 0 para sair]: '))
    if m == 0:
        break
    if m > len(lista):
          break
    print(f'As notas de {lista[m-1][0]} são: {lista[m-1][1]}')
    print('-' * 35)
print('Obrigado, volte sempre!')
 
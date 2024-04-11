pessoas = []
pesos = []
lista = []
while True:
    nome = (str(input('Digite o seu nome: ')))
    pessoas.append(nome)
    peso = (int(input('Digite o seu peso: ')))
    pesos.append(peso)

    per = str(input('Quer continuar?[S/N]: ')).upper()
    while per not in 'SN':
        per = str(input('Não entendi, quer continuar?[S/N]: ')).upper()
    if per == 'N':
        break

lista.append(pessoas[:])
print(f'Ao todo cadastrou {len(pessoas)} pessoas.')
maior = pesos.index(max(pesos))
print(f'O maior pesso foi de {max(pesos)}kg de {pessoas[maior]}.')
menor = pesos.index(min(pesos))
print(f'O menor pesso foi de {min(pesos)}kg de {pessoas[menor]}.')

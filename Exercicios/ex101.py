from datetime import date
def idade(ano):
    a = date.today().year
    s = a - p
    print(f'Com {s} anos, ', end='')
    if s < 18:
        return 'não tem direito a votar!'
    elif s >= 100:
        return 'o Voto é Opcional!'
    elif s >= 18:
        return 'é Obrigatório Votar!'

p = int(input('Qual o seu ano de nascimento?: '))
print(idade(p))

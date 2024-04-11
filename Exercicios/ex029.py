v = int(input('Digite a velocidade que passou na reta: '))
v2 = (v - 80) * 7
if v > 80:
    print(f'Você apanhou uma multa no valor de {v2}€')
else:
    print('Você viajava dentro dos limites de velocidade')

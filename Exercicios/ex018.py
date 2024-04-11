import math
a1 = float(input('Diga um valor para o ângulo: '))
c = math.cos(math.radians(a1))
s = math.sin(math.radians(a1))
t = math.tan(math.radians(a1))
print(f'O ângulo de {a1} tem o SENO de {s:.2}\nO ângulo de {a1} tem o COSSENO de {c:.2f}')
print(f'O ângulo de {a1} tem a TANGENTE de {t:.2f}')

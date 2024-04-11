import math
from math import sqrt
c1 = float(input('Cateto oposto do triângulo: '))
c2 = float(input('Cateto adjacente do triângulo: '))
h = (c1**2 + c2**2) ** (1/2)
print(f'O comprimento da hipotenusa é: {h:.2f}')

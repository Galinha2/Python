s = 0
v = 0
for c in range(0, 501, 3):
    if c % 2 > 0:
        s += c
        v += 1
print(f'A soma dos {v} valores é {s}')

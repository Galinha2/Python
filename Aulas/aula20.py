def dobro(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 3, 1, 0, 2]
dobro(valores)
print(valores)

v = []
for c in range(5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > v[-1]:
        v.append(n)
    else:
        p = 0
        while p < len(v):
            if n <= v[p]:
                v.insert(p, n)
                break
            p += 1
print(v)
#PRIMEIRO EX QUE NÃO EXECUTEI SOZINHO, NOTA 0!

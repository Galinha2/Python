def valor(n):
    return f'{n:.2f}€'.replace('.',',')
def dividir(n):
    t = n / 2
    return f'{t:.2f}€'.replace('.',',')
def multiplicar(n):
    t = n * 2
    return f'{t:.2f}€'.replace('.',',')

def dez(n, por):
    por = 1 + por / 100
    t = n * por
    return f'{t:.2f}€'.replace('.',',')

def menos(n, por):
    por = 1 - por / 100
    t = n * por
    return f'{t:.2f}€'.replace('.',',')

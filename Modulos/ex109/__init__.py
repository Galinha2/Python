def valor(n, tf = 0):
    if tf == False:
        return f'{n:.2f}€'
    elif tf == True:
        return f'{n:.2f}€'.replace('.',',')
def dividir(n, tf = 0):
    t = n / 2
    if tf == False:
        return f'{t:.2f}€'
    elif tf == True:
        return f'{t:.2f}€'.replace('.',',')
def multiplicar(n, tf = 0):
    t = n * 2
    if tf == False:
        return f'{t:.2f}€'
    elif tf == True:
        return f'{t:.2f}€'.replace('.',',')

def dez(n, por, tf = 0):
    por = 1 + por / 100
    t = n * por
    if tf == False:
        return f'{t:.2f}€'
    elif tf == True:
        return f'{t:.2f}€'.replace('.',',')

def menos(n, por, tf = 0):
    por = 1 - por / 100
    t = n * por
    if tf == False:
        return f'{t:.2f}€'
    elif tf == True:
        return f'{t:.2f}€'.replace('.',',')

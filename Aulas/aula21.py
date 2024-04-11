def contador(i, f, p):
    """
        Contagem de inicio ao fim por passos
        i: Inicio da contagem
        f: Fim da contagem
        p: Passo da contagem
        Função criada por Gustavo Guanabara do canal Curso em Video
    Returns:

    """
    while i <= f:
        print(i, end=' ')
        i += p

contador(2, 10, 2)
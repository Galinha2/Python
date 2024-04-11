from time import sleep

#FUNÇÃO para escrever pensar....
def pensando(pensa):
    sleep(0.3)
    print('PROCESSANDO', end=''), sleep(0.3)
    print('.', end=''), sleep(0.3)
    print('.', end=''), sleep(0.3)
    print('.', end=''), sleep(0.3)
    print('.'), sleep(0.3)


#Função que escreve e armazena o nome das pessoas e a sua idade.
def lista(nome):
    ficheiro = 'cursoemvideo.txt'
    nome = str(input('Digite o seu nome: ')).title().strip()
    idade = int(input('Digite a sua idade: '))

    with open(ficheiro, 'a') as file:
        file.write(f'{nome:<40}   {idade} anos\n')
        pensando(1)
        print()
        print(f'Novo registro de \033[36m{nome}\033[m adicionádo aos arquivos do sistema.')
        sleep(2)


#Função que apresenta a lista de pessoas cadastradas
def abrirlista():
    ficheiro = 'cursoemvideo.txt'
    with open(ficheiro, 'r') as file:
        conteudoficheiro = file.read()
        pensando(1)
        print()
        print(conteudoficheiro)
        sleep(2)


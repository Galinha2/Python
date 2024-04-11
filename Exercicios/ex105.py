from random import randint
def notas(*num, sit=False):
    '''

    ---> Função para analisar notas e situações de vários alunos.
        *num: Armazena as notas dos alunos
        sit: Se True avisa a situação do aluno, se False, remove a situação.
        Returns: Dicionário com todas as informações do aluno.

    '''
    dic = {'Total': len(num), 'Maior Nota': max(num), 'Menor Nota': min(num),
           'Média da Turma': sum(num) / len(num)}
    if sit == True:
        if sum(num) / len(num) < 10:
            dic['Situação'] = 'MÁ'
        elif sum(num) / len(num) <= 15:
            dic['Situação'] = 'BOA'
        elif sum(num) / len(num) > 15:
            dic['Situação'] = 'EXCELENTE'
    print(dic)
notas(randint(1,20), randint(1,20), randint(1,20), randint(1,20), sit=True)
#print(help(notas))

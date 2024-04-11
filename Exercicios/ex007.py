n1 = float(input('Digite a nota do seu primeiro exame: '))
n2 = float(input('Digite a nota do seu segundo exame: '))
m = (n1+n2)/2
s = n1+n2
print('A média de ambos os seus exames é: {:.2f}\nPois ({}+{}) dá: {}\nE {} a dividir por 2 exames é: {:.2f}'.format(m, n1, n2, s, s, m))
print('E assim se calcula a média!')

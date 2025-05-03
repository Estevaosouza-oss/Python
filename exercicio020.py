from random import shuffle
a1 = input("Digite o Nome do Aluno: ")
a2 = input("Digite o Nome do Aluno: ")
a3 = input("Digite o Nome do Aluno: ")
a4 = input("Digite o Nome do Aluno: ")

lista = [a1,a2,a3,a4]

shuffle(lista)

print('A ordem de aluno escolhido foi {}'.format(lista))

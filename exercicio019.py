from random import choice
alu1 = input('Primeiro Aluno: ')
alu2 = input('Segundo Aluno: ')
alu3 = input('Terceiro Aluno: ')
alu4 = input('Quarto Aluno: ')
lista = [alu1, alu2 ,alu3 ,alu4]
itema = choice(lista)

print ('O Aluno Escolhido foi {}'.format(itema))

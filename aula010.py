n1 = float(input("Digite a Primeira Nota: "))
n2 = float(input("Digite a Segunda Nota: "))
n3 = float(input("Digite a Terceiro Nota: "))
n4 = float(input("Digite a Quarto Nota: "))
 
m = (n1 + n2 + n3 + n4) / 4

print("A Primeira nota foi {}".format(n1))
print("A Segunda nota foi {}".format(n2))
print("A Terceiro nota foi {}".format(n3))
print("A Quarto nota foi {}".format(n4))
print('A Média das Notas foi {}'.format(m))

if m >= 7 :
    print ('Voce Passou!!!!')
elif m < 7  >= 5 :
    print('Voce Esta de Recuperação')
else :
    ('Voce Reprovou!!')

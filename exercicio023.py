num = int(input('Digite um Numero de até 4 digitos: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print ("Analisando o seu Numero {} ".format(num))
print ("Unidade {} ".format(u))
print ("Dezena {} ".format(d))
print ("Centena {} ".format(c))
print ("Milhar {} ".format(m))

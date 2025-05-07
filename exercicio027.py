nomec = str(input("Digite seu Nome Completo : ")).strip()
nomes = nomec.split()
print("Ola {} O Seu Primeiro nome é {}".format(nomec, nomes[0]))
print("O Seu Ultimo nome é {}".format( nomes[-1]))
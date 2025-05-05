nome = input("Digite seu Nome Completo: ").strip()

print ('Seu nome completo em Minusculo é {}'.format(nome.lower()))
print ('Seu nome completo em Maiusculo é {}'.format(nome.upper()))
print ('o Seu nome tem {} ao Todo'.format(len(nome) - nome.count(" ")))
print ('A Quantidade de Letras que seu primeiro nome tem são {} Letras'.format(nome.find(" ")))
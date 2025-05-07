frase = str(input("Digite uma Frase: ")).strip()
frasea = frase.upper()

print ('A Letra "A" aparece {} vezes '.format(frasea.count("A")))
print ('A Primeira Vez q a Letra "A" aparece é na posição {} '.format(frasea.find("A") +1))
print ('A Ultima Vez que a Letra "A" aparece é na posição {} '.format(frasea.rfind("A")+1))
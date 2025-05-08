from random import randint
naleatorio = randint (0 , 5)
nusuario = int(input('Digite um Numero inteiro entre 0 e 5: '))

if naleatorio == nusuario:
    print('Ual Parabens voce acertou')
else:
    print('Que Pena o Numero Escolhido foi {} Voce Errou!!'.format(naleatorio))

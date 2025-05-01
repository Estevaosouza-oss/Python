print ('==========================================')
print (' Olá como vai?')
print (' Antes de tudo')
nome = input (' Me diga primeiramente o seu nome: ')
print (' Ola',nome, 'Seja Bem vindo')
print (' Ao meu Primeiro Programa Python')
print (' Agora me diga...')
dia = int(input (' Qual o dia do seu nascimento? '))
if dia < 1 or dia > 31 :
        print ('Opa! o dia errado')
        fim = input(' Fim do programa aperte enter : ')
        print (fim)
        print ('==========================================')
else : mes = int(input (' certo... \n agora qual o seu mes de nascimento ? '))
if mes <1 or mes >12 :
        print ('Opa! o Mes Esta Errado!')
        fim = input(' Fim do programa aperte enter : ')
        print (fim)
        print ('==========================================')
else : ano = int(input (' Perfeito... \n Por fim... qual seu ano de nascimento? '))
if ano <1900 or ano >2025 :
        print : ('Acredito que o ano esta errado!')
        fim = input(' Fim do programa aperte enter : ')
        print (fim)
        print ('==========================================')
else:
        atual = 2025
        idade = atual - ano
        print ('==========================================')
        print (' entao', nome, 'voce nasceu em ',dia,'/',mes,'/',ano,'\n então nesse exato momento voce tem',idade, 'anos' )
        print ('==========================================')
fim = input(' Fim do programa aperte enter : ')
print (fim)
print ('==========================================')



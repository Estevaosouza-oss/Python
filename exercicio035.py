print ('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print ('       ANALISADOR DE TRIANGULO      ')
print ('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
tm1 = float(input('Digite o Primeiro Comprimento da Reta : '))
tm2 = float(input('Digite o Segundo Comprimento da Reta : '))
tm3 = float(input('Digite o Terceiro Comprimento da Reta : '))

if tm1 + tm2 > tm3 and tm2 + tm3 > tm1 and tm3 + tm1 > tm2 :
    print ("Essas Retas Formam um Triangulo")
else :
    print("Essas retas nao formam um Triangulo")
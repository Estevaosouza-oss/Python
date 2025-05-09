sala = float(input('Digite o Seu Salário: '))
if sala > 1250 :
    aumento = (sala * 0.1) + sala
    print ('O Seu Salário é R${:.2f} então voce recebera um aumento de 10%\n sendo assim seu salário passará a ser R${:.2f} '.format(sala,aumento))
else : 
    aumento = (sala * 0.15) + sala
    print ('O Seu Salário é R${:.2f} então voce recebera um aumento de 15%\n sendo assim seu salário passará a ser R${:.2f} '.format(sala,aumento))
    
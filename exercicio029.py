vcar = int(input("Me diga Qual foi a velocidade do Carro: "))
print('Analisando...')
if vcar > 80 :
    radar = vcar - 80
    multa = float (radar * 7)
    print("A sua Velocidade foi {} a mais do limite\n entao voce tera que pagar R${:.2f} de multa".format(radar, multa))
else :
    print('A que Bom! vc Estava dentro da velocidade Limite')
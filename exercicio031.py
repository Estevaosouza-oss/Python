viagem = float(input("Qual a Distancia da Kilometragem: "))

if viagem <= 200 :
    vvia = viagem * 0.45 
    print ("Voce vai viajar {} Km entao voce pagara R$0,45 por KM \nEntão voce tera que pagar R${:.2f} Pela Viagem".format(viagem, vvia))
else :
    viag = viagem * 0.5 
    print ('Voce vai viajar {} Km entao voce pagara R$0,50 por KM \nEntão voce tera que pagar R${:.2f} Pela Viagem'.format(viagem, viag))

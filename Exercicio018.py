from math import sin,cos,tan,radians
ang = float (input("Digite um angulo: "))
seno = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print ("Seu angulo escolhido foi o de {}º sendo assim".format(ang))
print ("O seu Seno é {:.2f}".format(seno))
print ("O seu Cosseno é {:.2f}".format(cos))
print ("e a sua Tangente é {:.2f} ".format(tan))

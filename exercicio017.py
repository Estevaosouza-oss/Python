from math import hypot
catop = float(input('Me diga qual Angulo do cateto Oposto: '))
catadj = float(input('Me diga qual Angulo do cateto Adjacente: '))
hip = hypot (catop, catadj)
#hip = (catop ** 2 + catadj ** 2) ** 0.5
print ("Seu catetto Oposto é {} \nseu cateto Adjacente é {} \nsendo assim a sua Hipotenuza é {:.2f}".format(catop,catadj,hip))

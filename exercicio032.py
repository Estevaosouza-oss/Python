from datetime import date
anobi = int(input('Qual o Ano que voce esta querendo saber, coloque "0" para ano atual : '))
if anobi == 0 :
    datatual = date.today().year
    print ('o ano de 2025 nao é Bissexto')

elif anobi % 4 == 0 and anobi % 100 != 0 or anobi % 400 == 0 :
    print ('o ano de {} é Bissexto!'.format(anobi))
else :
    print ('o ano de {} nao é Bissexto!'.format(anobi))
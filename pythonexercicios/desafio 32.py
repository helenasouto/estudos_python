from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual:'))
if ano == 0:
    ano = date.today().year
l = ano % 4
if l == 0 and ano % 100 !=0 or ano % 400 == 0:
    print('O ano de {} é BISSEXTO'.format(ano))
else:
    print('O ano de {} NÃO É BISSEXTO'.format(ano))


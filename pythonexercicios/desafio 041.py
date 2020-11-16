from datetime import date
atual = date.today().year
a = int(input('Digite o ano de nascimento do atleta:'))
i = atual - a
if i <= 9:
    print('A categoria é MIRIM')
if 9 < i <= 14:
    print('A categoria é INFANTIL')
if 14 < i <= 19:
    print('A categoria é JÚNIOR')
if 19 < i <= 20:
    print('A categoria é SÊNIOR')
if i > 20:
    print('A categoria é MASTER')
print('O atleta tem {} anos'.format(i))
# até: <=
#<=14
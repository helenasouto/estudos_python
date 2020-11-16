n = float(input('Qual é o preço do produto? R$'))
d = float(n-(n/100*5))
print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}'.format(n, d))




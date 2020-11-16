v = float(input('Qual é a distância da sua viagem?'))
print('Você está prestes a iniciar uma viagem de {}km'.format(v))
p1 = 0.50 * v
p2 = 0.45 * v
if v <= 200:
    print('E o preço da sua passagem será de R${:.2f}'.format(p1))
else:
    print('E o preço da sua passagem será de R${:.2f}'.format(p2))

n = float(input('Quanto dinheiro você tem na carteira? R$'))
d = float(n / 5.51)
e = float(n / 6.45)
print('Com R${:.2f} você pode comprar US${:.2f}'. format(n, d))
print('Com R${:.2f} você pode comprar {:.2f} euros'.format(n, e))










q = float(input('Quantos dias alugados? '))
k = float(input('Quantos Km rodados? '))
d = float(60*q)
f = float(0.15*k)
s = float(d+f)
print('O total a pagar é de R${:.2f}'.format(s))


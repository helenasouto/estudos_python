pn = float(input('Preço normal do produto:R$'))
f = str(input('Qual é a forma de pagamento'
'(dinheiro/cheque;cartão;2x no cartão;3x ou mais no cartão)?'))
v1 = (pn-(pn/100*10))
v2 = (pn-(pn/100*5))
if 'dinheiro/cheque':
    print('Se o pagamento for à vista, fica por R${:.2f}'.format(v1))
if 'cartão':
    print('Se o pagamento for à vista no cartão, o produto fica por R${:.2f}'.format(v2))
if '2x no cartão':
    print('Se o pagamento for em até 2 vezes no cartão o produto fica pelo preço normal:R${:.2f}'.format(pn))
if '3x ou mais no cartão':
    print(',,,')




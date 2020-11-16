va = float(input('Qual é o valor da casa?R$'))
s = float(input('Qual é o salário do comprador?R$'))
a = int(input('Em quantos anos planeja pagar?'))
p = va / (a * 12)
if p <= (s/100*30):
    print('\033[0;32mAprovado!')
    print('\033[mSerá possível comprar a casa')
else:
    print('\033[0;31mNegado!')
    print('\033[mNão será possível comprar a casa')
print('\033[0;35mO valor da prestação é de R${:.2f}'.format(p))







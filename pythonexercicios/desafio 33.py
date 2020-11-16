n1 = int(input('Primeiro valor:'))
n2 = int(input('Segundo valor:'))
n3 = int(input('Terceiro valor:'))
# Verificando quem é o menor
mn = n1
if n2 < n1 and n2 < n3:
    mn = n2
if n3 < n1 and n3 < n2:
    mn = n3
print('O menor valor digitado foi: {}'.format(mn))
# verificando quem é o menor
mi = n1
if n2>n1 and n2 >n3:
    mi = n2
if n3 > n1 and n3>n2:
    mi = n3
print('O maior valor digitado foi: {}'.format(mi))


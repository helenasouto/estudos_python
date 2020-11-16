a = float(input('Primeiro segmento:'))
b = float(input('Segundo segmento:'))
c = float(input('Terceiro segmento:'))
if a<b+c and b<c+a and c<b+a:
    print('Os segmentos acima PODEM FORMAR triângulo', end='')
    if a == b and a==c:
       print(' EQUILÁTERO')                                                    #a==b==c:
    elif a!= b and a!=c and c!=b:
        print(' ESCALENO!')
    else:
        print(' ISÓSCELES')
else:
    print('Os segmentos acima NÃO PODEM formar triângulo')

#,end=''Sem enter no fim da linha
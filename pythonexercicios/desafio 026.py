n = str(input('Digite uma frase:')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(n.count('A')))
print('a primeira letra A apareceu na posição {}'.format(n.find('A')+1))
print('A última letra A aparece na posição {}'.format(n.rfind('A')+1))

from random import shuffle
p = str(input('Primeiro aluno:'))
s = str(input('Segundo aluno:'))
t = str(input('Terceiro aluno:'))
q = str(input('Quarto aluno:'))
li = [p, s, t, q]
shuffle(li)
print('A ordem de apresentação será: ')
print(li)
# import random
# p = str(input('Primeiro aluno:'))
# s = str(input('Segundo aluno:'))
# t = str(input('Terceiro aluno:'))
# q = str(input('Quarto aluno:'))
# li = [p, s, t, q]
# random.shuffle(li)
# print('A ordem da apresentação será: ')
# print(li)

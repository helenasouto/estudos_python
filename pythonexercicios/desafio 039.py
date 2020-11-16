from datetime import date
atual = date.today().year
d = int(input('Informe seu ano de nascimento:'))
i = atual - d
# o = i - 18
# a= 18 - i
if i > 18:
    o = i - 18
    print('\033[0;31mPassou {} ano(s) do prazo para o alistamento'.format(o))
    f = atual - o
    print('Seu alistamento foi em {}'.format(f))
elif i < 18:
    a = 18 - i
    print('\033[0;34mAinda faltam {} ano(s) para se alistar ao serviço militar'.format(a))
    n = a + atual
    print('Seu alistamento será em {}'.format(n))
elif i == 18:
    print('\033[0;32mJá está na hora de se alistar!')
# elif or else

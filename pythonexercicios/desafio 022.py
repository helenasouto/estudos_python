f = str(input('Digite seu nome completo:')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas {}'.format(f.upper()))
print('Seu nome em minúsculas {}'.format(f.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(f)-f.count(' ')))
# print('Seu primeiro nome tem: {} letras.'.format(f.find(' ')))
separa = f.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))












print('\033[0;36m<<<'*5)
print('\033[1;33mCALCULE SEU IMC')
print('\033[0;36m>>>'*5)
p = float(input('\033[mDigite seu peso:(Kg)'))
a = float(input('Digite sua altura:(m)'))
imc = p / (a**2)
if imc<18.5:
    print('Seu IMC é de {:.1f} e você está \033[0;31mABAIXO DO PESO'.format(imc))
if 25>=imc>=18.5:
    print('Seu IMC é de {:.1f} e você está no \033[0;31mPESO IDEAL'.format(imc))
if 30<=imc<=40:
    print('Seu IMC é de {:.1f} e você está com \033[0;31mOBESIDADE'.format(imc))
if imc>40:
    print('Seu IMC é de {:.1f} e você está com \033[0;31mOBESIDADE MÓRBIDA'.format(imc))



vel = float(input('Qual é a velocidade atual do carro?'))
if vel <= 80:
    print('Tenha um bom dia! Dirija com segurança')
if vel > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    m = (vel-80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(m))

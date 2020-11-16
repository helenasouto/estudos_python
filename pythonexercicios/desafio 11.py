l: float = float(input('Largura da parede:'))
h: float = float(input('Altura da parede:'))
area = float(h*l)
t = float(area/2)
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(l, h, area))
print('Para pintar essa parede, você precisará de {}l de tinta'.format(t))









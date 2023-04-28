largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
print('Sua parede tem a dimensão de {:.1f}x{:.1f} e sua área é de {:.1f}m².'.format(largura, altura, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {:.1f}l de tinta.'.format(tinta))

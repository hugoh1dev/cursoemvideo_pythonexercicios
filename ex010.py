real = float(input('Quanto dinheiro você tem na carteira? '))
dolar = real / 5.25
euro = real / 5.58
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
print('Com R${:.2f} você pode comprar €{:.2f}'.format(real, euro))


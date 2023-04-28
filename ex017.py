'''
cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = ( cateto_oposto ** 2 + cateto_adjacente ** 2 ) ** (1/2)
print('A Hipotenusa vai medir {:.2f}.'.format(hipotenusa))
'''
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))


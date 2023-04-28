numero = int(input('Digite um numero para ver sua tabuada: '))
for cont in range(1, 11):
    print('{} x {:2} = {}'.format(numero, cont, numero*cont))

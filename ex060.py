'''
from math import factorial
num = int(input('Digite um numero para calcular seu fatorial: '))
f = factorial(num)
print(f'O fatorial de {num} é {f}.')'''

numero = int(input('Digite um numero para calcular seu fatorial: '))
contador = numero
fatorial = 1
print(f'Calculando {numero}! = ', end='')
while contador > 0:
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else ' = ', end= '')
    fatorial = fatorial * contador
    contador = contador - 1
print(f'{fatorial}.')

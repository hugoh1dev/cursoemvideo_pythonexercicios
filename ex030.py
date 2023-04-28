# Crie um programa que leia um número inteiro qualquer e mostre na tela
# se ele é PAR ou IMPAR.

numero = int(input('Me diga um número qualquer: '))
resultado = numero % 2
if resultado == 0:
    print('O Número {} é PAR!'.format(numero))
else:
    print('O Número {} é ÍMPAR!'.format(numero))

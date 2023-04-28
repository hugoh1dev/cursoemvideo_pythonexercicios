soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} números PARES e a soma é {}.'.format(cont, soma))

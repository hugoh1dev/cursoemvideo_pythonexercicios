num = list()
par = list()
impar = list()
while True:
    num.append(int(input('Digite um numero: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for indice, valor in enumerate(num):
    if valor % 2 == 0:
        par.append(valor)
    elif valor % 1 == 0:
        impar.append(valor)
print('-=' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')
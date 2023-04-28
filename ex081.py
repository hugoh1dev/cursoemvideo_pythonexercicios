numeros = []
while True:
    numeros.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Você digitou {len(numeros)} elementos')
numeros.sort(reverse=True)
print(f'Você digitou os valores {numeros}')
if 5 in numeros:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista.')
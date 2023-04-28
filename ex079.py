numeros = list()
while True:
    num = int(input('Digite um valor: '))
    if num not in numeros:
        numeros.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado, não vou adicionar...')
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
numeros.sort(reverse=True)
print(f'Você digitou os valores {numeros}')
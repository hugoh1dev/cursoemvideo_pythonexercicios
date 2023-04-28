temporario = []
principal = []
pesomaior = pesomenor = 0
while True:
    temporario.append(str(input('Nome: ')))
    temporario.append(float(input('Peso: ')))
    if len(principal) == 0:
        pesomaior = pesomenor = temporario[1]
    else:
        if temporario[1] > pesomaior:
            pesomaior = temporario[1]
        if temporario[1] < pesomenor:
            pesomenor = temporario[1]
    principal.append(temporario[:])
    temporario.clear()
    resposta = str(input('Quer Continuar? [S/N] '))
    if resposta in 'Nn':
        break

print('-=' * 30)
print(f'Os dados foram {principal}')
print(f'Ao todo você cadastrou {len(principal)} pessoas.')
print(f'O maior peso foi de {pesomaior}Kgs. Peso de ', end='')
for peso in principal:
    if peso[1] == pesomaior:
        print(f'{peso[0]} ', end='')
print()
print(f'O menor peso foi de {pesomenor}Kgs. Peso de ', end='')
for peso in principal:
    if peso[1] == pesomenor:
        print(f'{peso[0]} ', end='')
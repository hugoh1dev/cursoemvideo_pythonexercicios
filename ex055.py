pesomaior = 0
pesomenor = 0
for cont in range(1, 6):
    peso = float(input(f'Peso da {cont}ª pessoa: '))
    if cont == 1:
        pesomaior = peso
        pesomenor = peso
    else:
        if peso > pesomaior:
            pesomaior = peso
        if peso < pesomenor:
            pesomenor = peso
print(f'O maior peso lido foi de {pesomaior}Kg')
print(f'O menor peso lido foi de {pesomenor}Kg')

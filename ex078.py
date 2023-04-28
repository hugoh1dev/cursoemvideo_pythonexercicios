listanum = []
maiornum = 0
menornum = 0
for contador in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {contador}: ')))
    if contador == 0:
        maiornum = menornum = listanum[contador]
    else:
        if listanum[contador] > maiornum:
            maiornum = listanum[contador]
        if listanum[contador] < menornum:
            menornum =listanum[contador]
print('=-' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {maiornum} nas posições ', end='')
for indice, valor in enumerate(listanum):
    if valor == maiornum:
        print(f'{indice}...', end='')
print()
print(f'O menor valor digitado foi {menornum} nas posições ', end='')
for indice, valor in enumerate(listanum):
    if valor == menornum:
        print(f'{indice}...', end='')
print()

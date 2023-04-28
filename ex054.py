from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for cont in range(1, 8):
    nasc = int(input(f'Em que ano a {cont}ª nasceu? '))
    if atual - nasc >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print(f'Ao todo tivemos {totalmaior} pessoas maiores de idade.')
print(f'E também tivemos {totalmenor} pessoas menores de idade.')

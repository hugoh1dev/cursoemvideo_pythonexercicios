numero = [[], []]
valor = 0
for contador in range(1, 8):
    valor = int(input(f'Digite o {contador}o. valor: '))
    if valor % 2 == 0:
        numero[0].append(valor) 
    else:
        numero[1].append(valor)
print('-=' * 30)
numero[0].sort()
numero[1].sort()
print(f'Os valores pares digitados foram {numero[0]}')
print(f'Os valores impares digitados foram {numero[1]}')
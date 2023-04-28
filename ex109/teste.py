from moeda import aumentar, metade, dobro, diminuir

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda(p)} é {moeda(p)}')
print(f'O dobro de {moeda(p)} é {dobro(p, True)}')
print(f'Aumentando 10%, temos {aumentar(p, 10, True)}')
print(f'Diminuindo 13%, temos {diminuir(p, 13, True)}')
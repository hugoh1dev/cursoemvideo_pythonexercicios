from moeda import aumentar, metade, dobro, diminuir

preço = float(input('Digite o preço: R$'))
print(f'A metade de R${preço} é R${metade(preço, True)}')
print(f'O dobro de R${preço} é R${dobro(preço, True)}')
print(f'Aumentando 10%, temos R${aumentar(preço, 10, True)}')
print(f'Reduzindo 13%, temos R${diminuir(preço, 13, True)}')
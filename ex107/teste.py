from moeda import metade, dobro, aumentar, diminuir

preço = float(input('Digite o preço: R$'))
print(f'A metade de R${preço} é R${metade(preço)}')
print(f'O dobro de R${preço} é R${dobro(preço)}')
print(f'Aumentando 10%, temos R${aumentar(preço, 10)}')
print(f'Diminuindo 10%, temos R${diminuir(preço, 10)}')

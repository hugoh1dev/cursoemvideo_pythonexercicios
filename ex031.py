# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0.50 por Km para viagens de até 200Km
# e R$0.45 para viagens mais longas.

distancia = float(input('Qual é a distancia de sua viagem? '))
print('Você está perto de começar uma viagem de {}Km.'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('e o preço de sua passagem, será de R${:.2f}'.format(preco))


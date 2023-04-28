total = total1000 = menorpreço = contador = 0
barato = ''
while True:
    print('-' * 30)
    print('     LOJAS SUPER BARATÃO')
    print('-' * 30)
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    contador += 1
    total += preço
    if preço > 1000:
        total1000 += 1
    if contador == 1 or preço < menorpreço:
        menorpreço = preço
        barato = produto
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        print('{:-^40}'.format(' FIM DO PROGRAMA '))
        break
print(f'O total da compra foi de R${total}')
print(f'Temos {total1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} e custa R${menorpreço:.2f}')

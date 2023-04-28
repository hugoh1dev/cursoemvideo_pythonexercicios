def área(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno com uma {largura}x{comprimento} é de {a}m².')



print('Controle de terrenos')
print('-' * 20)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
área(largura, comprimento)
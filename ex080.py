lista = []
for cont in range(0, 5):
    num = int(input('Digite um valor: '))
    if cont == 0 or num > lista[len(lista)-1]:
        lista.append(num)
        print('Adicionado ao final da lista...')
    else:
        posição = 0
        while posição < len(lista):
            if num <= lista[posição]:
                lista.insert(posição, num)
                print(f'Adicionado na posição {posição} da lista.')
                break
            posição += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')
from time import sleep
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior 
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opção = int(input('>>>>>>>> Qual é a sua opção? ' ))
    if opção == 1:
        soma = num1 + num2
        print(f'A soma entre {num1} e {num2} é {soma}')
    elif opção == 2:
        multiplicar = num1 * num2
        print(f'O Resultado de {num1} x {num2} é {multiplicar}.')
    elif opção == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print(f'Entre {num1} e {num2} o maior valor é {maior}.')
    elif opção == 4:
        print('Informe os números novamente: ')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente! ')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre! ')

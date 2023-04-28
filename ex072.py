cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'catorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')
while True:
    while True:
        numero = int(input('Digite um numero entre 0 e 20: '))
        if 0 <= numero <= 20:
            break
        print('Tente novamente. ', end='')
    print(f'Você digitou o numero {cont[numero]}')
    print('')
    resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
       break
print('-' * 40)
print('Fim do Programa!')


from random import randint
vitoria = 0
print('=-' * 20)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-' * 20)
while True:
    computador = randint(0, 11)
    valor = int(input('Digite um valor: '))
    total = valor + computador
    pi = ' '
    while pi not in 'PI':
        pi = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    print('-' * 20)
    print(f'Você jogou {valor} e o computador {computador}. Total de {total} ')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    print('-' * 20)
    if pi == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vitoria += 1
        else:
            print('Você PERDEU!')
            break
    elif pi == 'I':
        if total % 1 == 0:
            print('Você VENCEU!')
            vitoria += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {vitoria} vezes.')

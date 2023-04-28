from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint (0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
sleep(0.5)
print('\033[33mJO\033[m')
sleep(0.5)
print('\033[33mKEN\033[m')
sleep(0.5)
print('\033[33mPO!!!\033[m')
print('-=' * 11)
print('O Computador jogou {}.'.format(itens[computador]))
print('O Jogador jogou {}.'.format(itens[jogador]))
print('-=' * 11)
if computador == 0:
    if jogador == 0:
        print('\033[34mEMPATE!\033[m')
    elif jogador == 1:
        print('JOGADOR \033[35mVENCE!\033[m')
    elif jogador == 2:
        print('COMPUTADOR \033[35mVENCE!\033[m')
    else:
        print('\033[31mJOGADA INVALIDA!\033[m')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR \033[35mVENCE!\033[m')
    elif jogador == 1:
        print('\033[34mEMPATE!\033[m')
    elif jogador == 2:
        print('JOGADOR \033[35mVENCE!\033[m')
    else:
        print('\033[31mJOGADA INVALIDA!\033[m')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR \033[35mVENCE!\033[m')
    elif jogador == 1:
        print('COMPUTADOR \033[35mVENCE!\033[m')
    elif jogador == 2:
        print('\033[34mEMPATE!\033[m')
    else:
        print('\033[31mJOGADA INVALIDA!\033[m')



# Escreva um programa que faça o computador "pensar" em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
# escolhido pelo computador
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
computador = randint (0, 5) # Faz o computador "PENSAR"
print('=' * 20)
print('\033[33mVou pensar em um número entre 0 e 5. Tente advinhar...\033[m')
print('=' * 20)
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta advinhar
print('\033[31mPROCESSANDO...\033[m')
sleep(3)
if jogador == computador:
    print('\033[1;37mPARABÉNS\033[m, você conseguiu me vencer!')
else:
    print('\033[1;37mGANHEI!\033[m Eu pensei no número\033[34m {}\033[m e não no \033[34m {}\033[m!'.format(computador, jogador))


from random import randint
from time import sleep
from operator import itemgetter
jogos1 = { 'Jogador 1': randint(1, 6),
          'Jogador 2': randint(1, 6),
          'Jogador 3': randint(1, 6),
          'Jogador 4': randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for keys, values in jogos1.items():
    print(f'{keys} tirou {values} no dado.')
    sleep(1)
ranking = sorted(jogos1.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('== RANKING DOS JOGADORES ==')
for indice, valor in enumerate(ranking):
    print(f'   {indice+1}º lugar: {valor[0]} com {valor[1]} pontos.')
    sleep(1)
jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: '))
total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for cont in range(0, total):
    partidas.append(int(input(f'    Quantos gols na partida {cont + 1}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
for keys, values in jogador.items():
    print(f'O campo {keys} tem o valor {values}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for indice, values in enumerate(jogador['gols']):
    print(f'    => Na partida {indice + 1}, fez {values} gols.')
print(f'Foi um total de {jogador["total"]} gols.')  

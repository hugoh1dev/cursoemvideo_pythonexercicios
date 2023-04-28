def ficha(jogos='<desconhecido>', gol=0):
    print(f'O Jogador {jogos} fez tantos {gol} gol(s) no campeonato.')


# Programa Principal
nome = str(input("Nome do Jogador: "))
gol = str(input("Número de Gols: "))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip() == '':
    ficha(gol=gol)
else:
    ficha(nome, gol)

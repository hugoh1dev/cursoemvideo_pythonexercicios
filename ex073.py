times = ('Corinthians', 'Bahia', 'Santos', 'São Paulo',
         'Atletico-MG', 'Atletico-PR', 'Fortaleza', 'Cruzeiro',
         'Vasco', 'Flamengo', 'Gremio', 'Botafogo',
         'America-MG', 'Coritiba', 'Fluminense', 'Goias',
         'Internacional', 'Palmeiras', 'Bragantino', 'Cuiaba')
print('-=' * 15)
print(f'Lista de times: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 ultimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabetica {sorted(times)}')
print('-=' * 15)
print(f'O Fortaleza está na {times.index("Fortaleza")+1}ª posição')

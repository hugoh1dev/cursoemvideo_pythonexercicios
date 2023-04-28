print('-=' * 20)
print('{: ^40}'.format('10 TERMOS DE UMA PA'))
print('-=' * 20)
termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
decimo = termo + (10 - 1) * razão
for cont in range(termo, decimo + razão, razão):
    print('{} '.format(cont), end=' →')
print('ACABOU!')
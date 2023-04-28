numprimo = int(input('Digite um número para verificarmos: '))
contprimo = 0
for c in range(1, numprimo + 1):
    if numprimo % c == 0:
        print('\033[33m', end='')
        contprimo = contprimo + 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi dividido {} vezes.'.format(numprimo, contprimo))
if contprimo == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele não é PRIMO!')
print('-' * 30)
print('Sequencia de Fibonacci')
print('-' * 30)
num = int(input('Quantos termos você quer mostrar? '))
termo1 = 0
termo2 = 1
print('~' * 30)
print(f'{termo1} → {termo2}', end='' )
cont = 3
while cont <= num:
    termo3 = termo1 + termo2
    print(f' → {termo3}', end='')
    termo1 = termo2
    termo2 = termo3
    cont += 1
print(' → FIM')
print('~' * 30)

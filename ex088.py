from random import randint
from time import sleep
lista = list()
jogos = list()
print('-=' * 30)
print('      JOGA NA MEGA SENA      ')
print('-=' * 30)
quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
totaljogos = 1
while totaljogos <= quantidade:
    contador = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)   
            contador += 1
        if contador >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    totaljogos += 1
print('-=' * 3, f'SORTEANDO {quantidade} JOGOS ', '-=' * 3)
for indice, lista in enumerate(jogos):
    print(f'Jogo {indice+1}: {lista}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
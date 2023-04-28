# Faça um programa que leia três números e mostre
# qual é o maior e qual é o menor.
primeiro_valor = int(input('Digite o primeiro valor: '))
segundo_valor = int(input('Digite o segundo valor: '))
terceiro_valor = int(input('Digite o terceiro valor: '))
# Verificando quem é o menor.
menor = primeiro_valor
if segundo_valor < primeiro_valor and segundo_valor < terceiro_valor:
    menor = segundo_valor
if terceiro_valor < primeiro_valor and terceiro_valor < segundo_valor:
    menor = terceiro_valor
print('O menor valor digitado foi {}'.format(menor))
# Verificando quem é o maior.
maior = primeiro_valor
if segundo_valor > primeiro_valor and segundo_valor > terceiro_valor:
    maior = segundo_valor
if terceiro_valor > primeiro_valor and terceiro_valor > segundo_valor:
    maior = terceiro_valor
print('O maior valor digitado foi {}'.format(maior))

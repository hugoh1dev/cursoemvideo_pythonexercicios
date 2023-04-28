maioridade = totalh = totalm = 0
while True:
    print('-' * 25)
    print('   CADASTRE UMA PESSOA   ')
    print('-' * 25)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('-' * 25)
    if idade >= 18:
        maioridade += 1
    if sexo == 'M':
        totalh += 1
    if sexo == 'F' and idade < 20:
        totalm += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maioridade}')
print(f'Ao todo temos {totalh} homens cadastrados.')
print(f'E temos {totalm} mulheres com menos de 20 anos.')
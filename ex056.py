somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
maioridademulher20 = 0
for pessoa in range(1, 5):
    print(f'----- {pessoa}ª PESSOA ------')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if pessoa == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridade = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        maioridademulher20 += 1
mediaidade = somaidade / 4
print(f'A média de idade do grupo é de {mediaidade} anos.')
print(f'O homem mais velho tem {maioridadehomem} e se chama {nomevelho}')
print(f'Ao todo são {maioridademulher20} mulheres com menos de 20 anos.')
linha1 = float(input('Primeiro segmento: '))
linha2 = float(input('Segundo segmento: '))
linha3 = float(input('Terceiro segmento: '))
if linha1 < linha2 + linha3 and linha2 < linha1 + linha3 and linha3 < linha2 + linha1:
    print('Os segmentos acima PODEM FORMAR um triangulo ', end='')
    if linha1 == linha2 == linha3:
        print('EQUILATERO!')
    elif linha1 != linha2 != linha3 != linha1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM formar um triangulo!')
# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se eles podem ou não formar um triângulo.

print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)
primeiro_segmento = float(input('Primeiro segmento: '))
segundo_segmento = float(input('Segundo segmento: '))
terceiro_segmento = float(input('Terceiro segmento: '))
if primeiro_segmento + segundo_segmento >= terceiro_segmento:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')

def escreva(mensagem):
    tamanho = len(mensagem) + 4
    print('~' * tamanho)
    print(f'  {mensagem}')
    print('~' * tamanho)


escreva('Hugo Junior')
escreva('Curso de Python no Youtube')
escreva('CeV')
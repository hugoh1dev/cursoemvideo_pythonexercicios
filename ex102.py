def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor fatorial de um número n.
    """
    f = 1
    for cont in range(n, 0, -1):
        if show:
            print(cont, end='')
            if cont > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= cont
    return f


print(fatorial(5, show=True))
help(fatorial)
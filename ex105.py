def notas(*name, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param name: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(name)
    r['maior'] = max(name)
    r['menor'] = min(name)
    r['media'] = sum(name)/len(name)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOAVEL'
        else:
            r['situação'] = 'RUIM'

    return r


# Programa Principal
resp = notas(10, 5.5, 4.5, 8.5, sit=True)
print(resp)
help(notas)
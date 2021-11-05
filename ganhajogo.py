def verifica_ganhador(x):

    for v,n in x.items():
        if len(n) == 0:
            return v

    return -1

def posicoes_possiveis(mesa, pecas):
    p_poss = []
    if len(mesa) == 0:
        for n in pecas:
            p_poss.append(pecas.index(n))
        return p_poss

    if len(mesa)== 1:
        for m in mesa:
            for p in pecas:
                if m[0] == p[1] or m[0] == p[0]:
                    p_poss.append(pecas.index(p))
                    print (p_poss)
                elif m[1] == p[1] or m[1] == p[0]:
                    p_poss.append(pecas.index(p))
                    print (p_poss)

    if len(mesa) > 1:
        w = len(mesa) - 1
        for p in pecas:
            if mesa[0][0] == p[0] or mesa[0][0] == p[1]:
                p_poss.append(pecas.index(p))
            elif mesa[0][1] == p[0] or mesa[0][1] == p[1]:
                p_poss.append(pecas.index(p))
                
            elif mesa[w][0] == p[0] or mesa[w][0] == p[1]:
                p_poss.append(pecas.index(p))
            elif mesa[w][1] == p[0] or mesa[w][1] == p[1]:
                p_poss.append(pecas.index(p))
                
        if len(p_poss) == 0:
            return p_poss
        
    return p_poss
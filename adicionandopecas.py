def adiciona_na_mesa(peca, mesa):
    #ex 1
    if len(mesa) == 0:
        mesa.append(peca)
        return mesa
    primeira_peca = mesa[0]
    ultima_peca = mesa[-1]
    #primeira peca igual primeira posicao:
    #ex 2
    if primeira_peca[0] == peca[1]:
        mesa.insert(0, peca)
        return mesa
    #ex 4
    if primeira_peca[0] == peca[0]:
        mesa.insert(0, [peca[1], peca[0]])
        return mesa
    #adiciona no final e inverte a peca
    if ultima_peca[1] == peca[1]:
        mesa.append([peca[1], peca[0]])             
        return mesa
    #sem inversao
    if ultima_peca[1] == peca[0]:
        mesa.append(peca)
        return mesa    

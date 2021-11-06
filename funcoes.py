#Primera Funcao
import random
def cria_pecas():
    i = 0
    comp = []
    while i <= 6:
        x = i
        while x <= 6:
            peca = [i, x]
            comp.append(peca)
            x += 1
        i += 1
    random.shuffle(comp)
    return (comp)

#Segunda Funcao
def inicia_jogo(jog, pecas):
    jogo = {
        'jogadores':{
        },
        'monte': [
        ],
        'mesa': [
        ]
    }
    i = 0
    while i < jog:
        jogo['jogadores'][i] = []
        i += 1  
    i = 0
    for p in pecas:
        if i == jog:
            jogo['monte'].append(p)
        else:
            jogo['jogadores'][i].append(p)
    
            if len(jogo['jogadores'][i]) == 7:   
                
                i += 1
    return jogo

#Terceira Funcao
def verifica_ganhador(x):

    for v,n in x.items():
        if len(n) == 0:
            return v

    return -1

#Quarta Funcao
def soma_pecas(x):
    soma = 0
    for n in x:
        soma += n[0] + n[1]

    return soma

#Quinta Funcao
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

#Sexta Funcao
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

def inicia_jogo(jog, pecas):
    jogo = {
        'jogadores':{
        
        },
        'monte':[
        
        ],
        'mesa':[

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

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
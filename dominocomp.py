import random
from funcoes import *
import sys

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

print (BLUE + 'Bem-vindo ao Jogo de Dominó P&R, onde a sua experiência será exatamente a mesma do jogo normal, porém no terminal de um computador!!' + RESET)
#Comeco do Jogo
comeca = input(CYAN + 'Você quer Joga[S/N]:' + RESET)

com =True

while com:
    if comeca == 'N':
        print (RED + 'Ta boa então! Bom Dia, Boa Tarde e Boa Noite. Ate a Próxima!' + RESET)
        sys.exit()
    elif comeca == 'S':
        pecas_c = cria_pecas()
        com = False
    else:
        print(RED + 'INVÁLIDO, TENTAR NOVAMENTE' + RESET)
        comeca  = input(CYAN + 'Você quer Joga[S/N]:' + RESET)

jogo = True
con = True
while jogo:
    
    while con:
        n_player = int(input('Quantos Jogadores[2-4]:'))
        if n_player not in range(2,4):
            print(RED + 'NÚMERO INVÁLIDO' + RESET)
            n_player = int(input('Quantos Jogadores[2-4]:'))
        else:
            inicia = inicia_jogo(n_player, pecas_c)
            con = False

    #Jogo Iniciado
    rodando = True
    i = 0
    while rodando:
        emp = 0
        mesa = inicia['mesa']
        player = inicia['jogadores']
        monte = inicia['monte']
        if i == 0:
            #jogador 1(Jogador IRL) - falta deixar bonito
            print(f'Sua mão: {player[i]}\n')
            joga_0 = posicoes_possiveis(mesa,player[i])
            print (f'Escolha um peça para jogar: {joga_0}\n')

            if len(joga_0) == 0:
                pegando_do_monte(monte, player[i])
                print(BOLD + 'Você pegou uma peça do monte' + RESET)
                print(f'Sua mão: {player[i]}\n')
                joga_0 = posicoes_possiveis(mesa,player[i])
                print (f'Escolha um peça para jogar: {joga_0}\n')

            if len(joga_0) == 0:
                print(RED + 'Você não tem peças para jogar' + RESET)
                i += 1
                emp += 1
            else:
                col = int(input('Qual peça deseja colocar?: '))
                peca = player[i][col]
                adiciona_na_mesa(peca, mesa)
                del player[i][col]
                print(f'mesa: {mesa}\n')
                i += 1

        while i < n_player:
            poss_bot = posicoes_possiveis(mesa,player[i])
            if len(poss_bot) == 0:
                pegando_do_monte(monte, player[i])
                print(BOLD + f'Jogador {i} pegou uma peça do monte' + RESET)
                poss_bot = posicoes_possiveis(mesa,player[i])
            
            if len(poss_bot) == 0:
                i += 1
                emp += 1
            else:
                p_q_joga = random.randint(0 , len(poss_bot)-1)
                peca = player[i][p_q_joga]
                adiciona_na_mesa(peca, mesa)
                del player[i][p_q_joga]
                print(f'mesa: {mesa}\n')
                i += 1
        ganhou = verifica_ganhador(player)
        if ganhou != -1:
            print(f"Jogador {ganhou+1} ganhou o jogo")
            rodando = False



        if emp == n_player:
            y = 0
            
            soma = soma_pecas (player[y])
            n = soma
            y += 1
            while y < n_player:
                soma = soma_pecas (player[y])
                print(f'Jogador {y+1} tem {soma} pontos en sua mao')
                if n == soma:
                    y += 1
                else: 
                    if soma < y:
                        n = soma
                        x = (f'Jogador {y + 1} ganhou com {n} pontos!')
                        y += 1

            print (x)
            rodando = False
        i = 0
    
    x = input('Quer jogar denovo?[S/N]: \n')
    if x == 'S':
        con = True
    elif x == 'N':
        print('Muito Obrigado por jogar')
        jogo = False
    else:
        print (RED + 'RESPOSTA NÃo VAlÍDA')




    


        
        
        



        









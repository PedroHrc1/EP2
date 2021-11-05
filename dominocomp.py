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

com = True

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

con = True
while con:
    x = int(input('Quantos Jogadores[2-4]:'))
    if x not in range(2,4):
        print(RED + 'NÚMERO INVÁLIDO' + RESET)
        x = int(input('Quantos Jogadores[2-4]:'))
    else:
        inicia = inicia_jogo(x, pecas_c)
        con = False

#Jogo Iniciado
rodando = True
i = 0
while rodando:
    if i == 0:
        print(inicia['jogadores'][i])
        print (posicoes_possiveis(inicia['mesa'],inicia['jogadores'][i]))
        colocando = int(input('Qual peça deseja colocar?:'))
        inicia['mesa'].append(inicia['jogadores'][i].index(colocando))
        print (inicia['mesa'])
        rodando = False









#====================================== Instituição ==========================================
# Centro Universitário FEI
# Data: 13/05/2021
#=============================================================================================
#====================================== DEV'S ================================================
# Murilo Lameira       | R.A: 22.120.008-2
#----------------------+-------------------
# Guilherme Brigagão   | R.A: 22.120.071-0
#----------------------+-------------------
# Zairon  Lincoln      | R.A: 22.119.069-7
#=============================================================================================
#==================================== IMPORTS ================================================

import datetime
import os
from colorama.ansi import Fore
import Parte_1 #Chama as funções feitas para a parte 1 do projeto 
import Parte_2 #Chama as funções feitas para a parte 2 do projeto

#=============================================================================================

#==================================== MENU ===================================================
def Menu():
    print(60*"=")
    print("Projeto 3 de CF3121 versão 1.0.0")
    print(60*"=") 
    comando = int(input('''
        [1] Calcular a Energia de um Fóton 
        [2] Valor do Número Quântico 'n'
        [3] Entrada do Estado 'ni' inicial e Estado final 'nf'
        [4] 5 Séries do Hidrogênio
        [5] Fóton Incidente no Átomo de Hidrogênio

        [9] Informações sobre o sistema
        [0] Sair
                        
        Qaul opção deseja: '''))
    print(60*"=")
    
    
    match comando:   
        case 1:
            Parte_1.Energia_Foton()

        case 2:
            Parte_1.Numero_Quantico()
    
        case 3:
            Parte_2.n_emi_abs()

        case 4:
            Parte_2.serie_hidro()
    
        case 5:
            Parte_2.foton_incid()

        case 9:
            Parte_1.infos()

        case 0:
            print(60*"=")
            print("Tchau, até logo!")
            print("Obrigado Pela Preferência! ")
            print(60*"=")

    if comando > 9 or comando < 0:
        print(60*"=")
        print("Tente outro Número!")
        print(60*"=")
        Menu()

#=============================================================================================

#==================================== FUNÇÃO PRINCIPAL =======================================

def Main():
    data_atual = datetime.date.today() # Data atual
    print(60*"=")
    print(Fore.RED + "Bem vindo!" + Fore.RESET)
    print(60*"=")
    print("Data: " + Fore.CYAN + "{}".format(data_atual.strftime('%d/%m/%Y')) + Fore.RESET) #imprime a data atual
    
    Menu()

os.system("cls")#limpa a tela

if __name__ == "__main__":
    Main()

#=============================================================================================


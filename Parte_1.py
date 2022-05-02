#==================================== IMPORTS ================================================
import time
import os
import math
from colorama import Fore
import Projeto_Main
#=============================================================================================

#==================================== VARIAVEIS UNIVERSAIS ===================================
c = 2.9792E8    # Velocidade da luz em metros por segundos 
h = 4.136E-15   # Constante de Planck em [Ev]
q = 1.6021E-19  # Carga Elementar
me = 9.1093E-31 # Massa do elétron em microgramas
R = 1.0973E7    # Constante de Rydberg
E0 = 8.8541E-12 # Constante de permissividade do vácuo
n = 1           # Número Quântico 
pi = math.pi    # Valor de pi
a0 = 5.2917E-11 # Raio de Bohr

#=============================================================================================

#==================================== FORMULAS ===============================================
Kn = (1 / E0**2)*((me*q**4) / (8*n**2*h**2))       # Energia Cinética de Bohr
Un = -(1 / E0**2)*((me*q**4) / (4*n**2*h**2))      # Energia Potencial de Bohr
En = Kn + Un                                      # Energia Total de Bohr
rn = E0 * ((n**2 * h**2) / pi * me * q**2)         # Raio da Orbita de Bohr
Vn = (1 / E0) * (q**2/2*n*h)                       # Velocidade Orbital de Bohr
Br = h/me * Vn                                    # comprimento de onda de De Broglie
#=============================================================================================



#==================================== FUNÇÃO ENERGIA FOTON ===================================
def Energia_Foton():
    global c, h #Variaveis Universais
    print()
    print(Fore.RED + "    ENERGIA FÓTON" + Fore.RESET)
    print()
    print(60*"=")
    print('''
    [1] Frequência 'f'
    [2] Comprimento de onda 'λ'

    [0]Cancelar operação
    ''')
    
    print(60*"=")
    comando = int(input("Digite a sua opção: "))
    print(60*"=")
    if comando == 1: 
        f = float(input("Qual sua frequência: "))
        eV = h * f 
        J  = (6.26E-34 * f) 
        print("------------------+-------------------------") 
        print("Energia do Fóton: |  " + Fore.YELLOW + "{:.4E}".format(eV) + Fore.RESET +" Hz")
        print("------------------+-------------------------")
        print("Energia do Fóton: |  " + Fore.YELLOW + "{:.4E}".format(J) + Fore.RESET +" J")
        print(60*"=")
        print("Voltando para o Menu...")
        time.sleep(10)
        return Projeto_Main.Menu()

    elif comando == 2:
        λ = float(input("Qual seu Comprimento de onda: "))
        eV = (h * c) / λ
        J  = (6.26E-34 * c) / λ
        print("------------------+-------------------------")
        print("Energia do Fóton: |  " + Fore.YELLOW + "{:.4E}".format(eV) + Fore.RESET + " eV")
        print("------------------+-------------------------")
        print("Energia do Fóton: |  " + Fore.YELLOW + "{:.4E}".format(J) + Fore.RESET + " J")
        print(60*"=")
        print("Voltando para o Menu...")
        time.sleep(10)
        return Projeto_Main.Menu()

    elif comando == 0:
        print(60*"=")
        print("Voltando para o Menu...")
        time.sleep(2)
        
        print(60*"=")
        return Projeto_Main.Menu()

    else:
        print(60*"=")
        print("Tente outro Número!")
        print(60*"=")
        return Energia_Foton()

#=============================================================================================

#==================================== FUNÇÃO NUMERO QUANTICO =================================
def Numero_Quantico():
    global c, h, Kn, Un, En, rn, Vn, Br, n #Variaveis Universais
    print()
    print( Fore.RED + "   NÚMERO QUÂNTICO" + Fore.RESET)
    print()
    print(60*"=")
    n = int(input("Digite o número quântico do átomo de hidrogênio: "))
    print(60*"=")
    
    print("Energia cinética do elétron:                      |  " + Fore.YELLOW + "{:.4E}".format(Kn) + Fore.RESET +" eV")
    print("--------------------------------------------------+--------")
    print("Energia potencial do elétron:                     |  " + Fore.YELLOW + "{:.4E}".format(Un) + Fore.RESET +" eV")
    print("--------------------------------------------------+--------")
    print("Energia total do átomo:                           |  " + Fore.YELLOW + "{:.4E}".format(En) + Fore.RESET +" eV")
    print("--------------------------------------------------+--------")
    print("Raio da órbita do elétron no átomo de hidrogênio: |  " + Fore.YELLOW + "{:.4E}".format(rn - 10E-9) + Fore.RESET +" nm")
    print("--------------------------------------------------+--------")
    print("Velocidade do elétron na órbita:                  |  " + Fore.YELLOW + "{:.4E}".format(Vn) + Fore.RESET +" m/s")
    print("--------------------------------------------------+--------")
    print("Comprimento de onda de De Broglie:                |  " + Fore.YELLOW + "{:.4E}".format(Br) + Fore.RESET +" λ")
    print(60*"=")
    return Projeto_Main.Menu()

#=============================================================================================

#==================================== Informações ============================================
def infos():
    os.system("cls")#limpa a tela
    time.sleep(1)
    print("====================================== Instituição ==========================================")    
    print(" Centro Universitário FEI                                                                    ")
    print("---------------------------------------------------------------------------------------------")
    print(" CF3121                                                                                      ")
    print("---------------------------------------------------------------------------------------------")
    print(" Projeto 3: Átomo de hidrogênio e quantização de energia                                     ")
    print("---------------------------------------------------------------------------------------------")  
    print("=============================================================================================")
    print("====================================== DEV'S ================================================")
    print(" Murilo Lameira       | R.A: 22.120.008-2 |                                                  ")
    print("----------------------+-------------------+--                                                ")
    print(" Guilherme Brigagão   | R.A: 22.120.071-0 |                                                  ")
    print("----------------------+-------------------+--                                                ")
    print(" Zairon Lincoln       | R.A: 22.119.069-7 |                                                  ")
    print("=============================================================================================")
    print("====================================== Informações ==========================================")
    print(" Data:  13/05/2021                                                                           ") 
    print("---------------------------------------------------------------------------------------------")
    print(" Versão: 1.0.0                                                                               ")
    print("=============================================================================================")
    comando = str(input(" Deseja Voltar ao menu? [SIM/NAO]\n ")).strip().upper()
    print("=============================================================================================")

    if comando == "SIM":
        print("Voltando para o menu...")
        return Projeto_Main.Menu()
    
    elif comando == "NAO":
        print("Tchau, até logo!")
        print("Obrigado Pela Preferência! ")
        print("=============================================================================================")       
        return quit()


#=============================================================================================


#==================================== IMPORTS ================================================
import datetime
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
data_atual = datetime.date.today() # Data atual
#=============================================================================================

#==================================== FORMULAS ===============================================
Kn = (1 / E0**2)*((me*q**4) / (8*n**2*h**2))       # Energia Cinética de Bohr
Un = -(1 / E0**2)*((me*q**4) / (4*n**2*h**2))      # Energia Potencial de Bohr
En = Kn + Un                                       # Energia Total de Bohr
rn = E0 * ((n**2 * h**2) / pi * me * q**2)         # Raio da Orbita de Bohr
Vn = (1 / E0) * (q**2/2*n*h)                       # Velocidade Orbital de Bohr
Br = h/me * Vn                                     # comprimento de onda de De Broglie

#=============================================================================================

#================================== EMISSÃO E ABSORÇÃO =======================================
def n_emi_abs():
    print()
    print(Fore.RED  + "    EMISSÃO E ABSORÇÃO" + Fore.RESET)
    print()
    print(60*"=")
    ni = int(input("Valor da transição de um nível inicial 'ni': "))
    print(60*"-") 
    
    if ni == 1:
        ni = -13.6
        
    elif ni == 2:
        ni = -3.4
        
    elif ni == 3:
        ni = -1.54
        
    elif ni == 4:
        ni = -0.85
        
    elif ni == 5:
        ni = -0.54
        
    elif ni == 6:
        ni = -0.38
        
    elif ni == 7:
        ni = -0.28
        
    nf = int(input("Valor da transição do nível final 'nf': "))

    if nf == 1:
        nf = -13.6
        
    elif nf == 2:
        nf = -3.4
        
    elif nf == 3:
        nf == -1.54
        
    elif nf == 4:
        nf = -0.85
        
    elif nf == 5:
        nf = -0.54
        
    elif nf == 6:
        nf = -0.38
        
    elif nf == 7:
        nf = -0.28

    # FORMULAS AUX    
    nt = ni - nf       # n = número quantico
    ei = -13.6/ni**2   # e = energia
    ef = -13.6/nf**2
    e = ei - ef
    λ = (4.136E-15 * 3E8)/e
    if (nt > 0):
        print(60*"-")
        print('Um fóton de ' + Fore.YELLOW + '{:.4E}'.format(λ  - 10E-9) + Fore.RESET + ' nm é emitido na transição')
        print(60*"=")
        time.sleep(5)
        Projeto_Main.Menu

    elif (nt < 0):
        print(60*"-")
        print('Um fóton de ' + Fore.YELLOW + '{:.4E}'.format((λ * -1) - 10E-9) + Fore.RESET + ' nm é absorvido na transição')
        print(60*"=")
        time.sleep(5)
        Projeto_Main.Menu

#=============================================================================================

#================================== SÉRIES DO HIDROGÊNIO =====================================
def serie_hidro():
    global R, c

    print()
    print(Fore.RED  + "    5 SÉRIES DO HIDROGÊNIO" + Fore.RESET)
    print()
    print(60*"=")
    print('''
    [1] Lyman
    [2] Balmer
    [3] Paschen
    [4] Brackett
    [5] Pfund

    [0] Sair
    ''')
    print(60*"=")
    comando = int(input("Digite a sua opção: "))
    print(60*"=")
    n = int(input("Digitar o número quântico ni inicial "))

    if comando == 1:
        #Lyman
        λ = 1/(R*((1/1**2)-(1/n**2)))
        f = c/λ
        print("Comprimento de onda :                |  " + Fore.YELLOW + "{:.4E}".format(λ) + Fore.RESET +" λ")
        print("-------------------------------------+--------------------")
        print("Frequência da onda  :                |  " + Fore.YELLOW + "{:.4E}".format(f) + Fore.RESET +" Hz")
        print("-------------------------------------+--------------------")
        #espectro de cores visíveis
        if f == 656.3E-9 :
            print("O fóton emite uma cor:               |  " + Fore.RED + "Vermelho" + Fore.RESET)
        elif f == 486.1 :
            print("O fóton emite uma cor:               |  " + Fore.GREEN + "Verde" + Fore.RESET)
        elif f == 434.1 :
            print("O fóton emite uma cor:               |  " + Fore.BLUE + "Azul" + Fore.RESET)
        elif f == 410.2 :
            print("O fóton emite uma cor:               |  " + Fore.MAGENTA + "Violeta" + Fore.RESET)
        time.sleep(30)
        Projeto_Main.Menu()

    elif comando == 2:
        #balmer
        λ = 1/(R*((1/2**2)-(1/n**2)))
        f = c/λ
        print("Comprimento de onda :                |  " + Fore.YELLOW + "{:.4E}".format(λ) + Fore.RESET +" λ")
        print("-------------------------------------+--------------------")
        print("Frequência da onda  :                |  " + Fore.YELLOW + "{:.4E}".format(f) + Fore.RESET +" Hz")
        print("-------------------------------------+--------------------")
        #espectro de cores visíveis
        if f == 656.3E-9 :
            print("O fóton emite uma cor:               |  " + Fore.RED + "Vermelho" + Fore.RESET)
        elif f == 486.1E-9 :
            print("O fóton emite uma cor:               |  " + Fore.GREEN + "Verde" + Fore.RESET)
        elif f == 434.1E-9 :
            print("O fóton emite uma cor:               |  " + Fore.BLUE + "Azul" + Fore.RESET)
        elif f == 410.2E-9 :
            print("O fóton emite uma cor:               |  " + Fore.MAGENTA + "Violeta" + Fore.RESET)
        time.sleep(30)
        Projeto_Main.Menu()

    elif comando == 3:
        #Paschen
        λ = 1/(R*((1/3**2)-(1/n**2)))
        f = c/λ
        print("Comprimento de onda :                |  " + Fore.YELLOW + "{:.4E}".format(λ) + Fore.RESET +" λ")
        print("-------------------------------------+--------------------")
        print("Frequência da onda  :                |  " + Fore.YELLOW + "{:.4E}".format(f) + Fore.RESET +" Hz")
        print("-------------------------------------+--------------------")
        #espectro de cores visíveis
        if f == 656.3E-9 :
            print("O fóton emite uma cor:               |  " + Fore.RED + "Vermelho" + Fore.RESET)
        elif f == 486.1E-9 :
            print("O fóton emite uma cor:               |  " + Fore.GREEN + "Verde" + Fore.RESET)
        elif f == 434.1E-9 :
            print("O fóton emite uma cor:               |  " + Fore.BLUE + "Azul" + Fore.RESET)
        elif f == 410.2E-9 :
            print("O fóton emite uma cor:               |  " + Fore.MAGENTA + "Violeta" + Fore.RESET)
        time.sleep(30)
        Projeto_Main.Menu()

    elif comando == 4:
        #Brackett
        λ = 1/(R*((1/4**2)-(1/n**2)))
        f = c/λ
        print("Comprimento de onda :                |  " + Fore.YELLOW + "{:.4E}".format(λ) + Fore.RESET +" λ")
        print("-------------------------------------+--------------------")
        print("Frequência da onda  :                |  " + Fore.YELLOW + "{:.4E}".format(f) + Fore.RESET +" Hz")
        print("-------------------------------------+--------------------")
        #espectro de cores visíveis
        if f == 656.3E-9 :
            print("O fóton emite uma cor:               |  " + Fore.RED + "Vermelho" + Fore.RESET)
        elif f == 486.1E-9 :
            print("O fóton emite uma cor:               |  " + Fore.GREEN + "Verde" + Fore.RESET)
        elif f == 434.1E-9 :
            print("O fóton emite uma cor:               |  " + Fore.BLUE + "Azul" + Fore.RESET)
        elif f == 410.2E-9 :
            print("O fóton emite uma cor:               |  " + Fore.MAGENTA + "Violeta" + Fore.RESET)
        time.sleep(30)
        Projeto_Main.Menu()

    elif comando == 5:
        #Pfund
        λ = 1/(R*((1/5**2)-(1/n**2)))
        f = c/λ
        print("Comprimento de onda :                |  " + Fore.YELLOW + "{:.4E}".format(λ) + Fore.RESET +" λ")
        print("-------------------------------------+--------------------")
        print("Frequência da onda  :                |  " + Fore.YELLOW + "{:.4E}".format(f) + Fore.RESET +" Hz")
        print("-------------------------------------+--------------------")
        #espectro de cores visíveis
        if f == 656.3E-9 :
            print("O fóton emite uma cor:               |  " + Fore.RED + "Vermelho" + Fore.RESET)
        elif f == 486.1E-9 :
            print("O fóton emite uma cor:               |  " + Fore.GREEN + "Verde" + Fore.RESET)
        elif f == 434.1E-9 :
            print("O fóton emite uma cor:               |  " + Fore.BLUE + "Azul" + Fore.RESET)
        elif f == 410.2E-9 :
            print("O fóton emite uma cor:               |  " + Fore.MAGENTA + "Violeta" + Fore.RESET)
        time.sleep(30)
        Projeto_Main.Menu()

    elif comando == 0:
        print(60*"=")
        print("Voltando para o Menu...")
        time.sleep(3)
        print(60*"=")
        return Projeto_Main.Menu()

    else:
        print(60*"=")
        print("Tente outro Número!")
        print(60*"=")
        return serie_hidro() 

#=============================================================================================

#================================== fóton que incide no átomo de hidrogênio ==================
def foton_incid():
    global R, c
    
    λ = float(input("Digite o comprimento da onda que irá incidir no atomo de hidrogenio em nm: "))
    ni = 0
    e = (4.136E-15 * 3E8)/λ
    ei = -13.6
    ef = ei - e
    nf = (-13.6/ef)
    resultado = nf**2
    nt = ni - resultado       # n = número quantico
    
    if (nt > 0):
        print(60*"-")
        print('O átomo será: ' + Fore.BLUE + 'Ionizado' + Fore.RESET)
        print(60*"-")
        print('O valor de nf do elétron: ' + Fore.YELLOW + '{:.0f}'.format(resultado) + Fore.RESET)
        print(60*"=")
        time.sleep(5)
        Projeto_Main.Menu
    
    elif (nt < 0):
        print(60*"-")
        print('O átomo é absorvido')
        print(60*"-")
        print('O valor de nf do elétron: ' + Fore.YELLOW + '{:.0f}'.format(resultado) + Fore.RESET)
        print(60*"=")
        time.sleep(5)
        Projeto_Main.Menu
    

#=============================================================================================
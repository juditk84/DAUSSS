import random

GUANYES = (7, 11)
PERDS = (2,3,12)

def tirarDaus():
    dau1 = random.randrange(1,6)
    dau2 = random.randrange(1,6)

    return dau1 + dau2


def Comprovar(tirada):
   
    if tirada in GUANYES:
        return "G"

    elif tirada in PERDS:       
        return "P"
    
    else:
        return "T"
        

def SeguirJugant(tirada):

    if tirada + tirarDaus() >= 15:
        return "G"
    
    else:
        return "P"

game_runs = ""

while game_runs != "no":

    primera_tirada = tirarDaus() # ho faig així perquè penso que igual em farà falta tenir el primer resultat stored de cara a SeguirJugant()

    if Comprovar(primera_tirada) == "G":
        print(f"oye, a la primera tirada has tret un {primera_tirada}. Vaya crack, ojalá tot tan fàcil, eh?")

    elif Comprovar(primera_tirada) == "P":
        print(f"pos res, has tret un {primera_tirada}. No et vull desmotivar, però quin fracàs.")

    else:
        print(f"goita! Com has tret un {primera_tirada} tens dret a tornar a tirar. #totaniràbé")
        input("(tornes a tirar els daus. Apreta qualsevol tecla per veure qué ha pasao.)")
        
        SeguirJugant(primera_tirada) # no estic segura de si hauria d'store això en una variable. Maybe?

        if SeguirJugant(primera_tirada) == "G":
            print("a la segona va la vencida! Sempre entenia BALA VENCIDA de peque, whatever that means.")
        else:
            print("ni amb una segona tirada. Què pringui. No me llames más.")
            
    game_runs = input("vols tornar a jugar, AMOR MÍO?\n\n\t(\"no\" per sortir d'aquest dice hell)\n")

    if game_runs == "no":
        break
import random

    # es tiren dos daus de 6 cares. Si A LA PRIMERA TIRADA sumen 7 o 11, el jugador guanya directament.
    # si A LA PRIMERA TIRADA dona 2, 3 o 12, perd directament.
    # else: es tira un segon cop. Si la suma primera+segona tirada és >= 15, guanya. Si no, perd.
guanyes = [7, 11]
perds = [2,3,12]

def tirarDaus():
    dau1 = random.randrange(1,6)
    dau2 = random.randrange(1,6)
    return dau1 + dau2

def Comprovar(func):
    if func in guanyes:
        print(func)
        return print("G")

    elif func in perds:
        print(func)        
        return print("P")
    else:
        SeguirJugant(func)
        

def SeguirJugant(primera_tirada):
    
    print("T")

    if primera_tirada + tirarDaus() >= 15:
        return "G"
    else:
        return "P"

Comprovar(tirarDaus())
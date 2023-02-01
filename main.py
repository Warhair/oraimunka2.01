#Megoldás
jatekos = [3,4,5,6,7]
gep = []

def osszegzes(lapok):
    osszeg = 0
    for i in lapok:
        osszeg += i

    return osszeg


def eredmény(jatekos: list, gep: list):
    eredmeny = ""
    if osszegzes(jatekos) > 21 and osszegzes(gep) > 21:
        eredmeny = "Döntetlen"
        return eredmeny

    elif osszegzes(jatekos) > 21:
        eredmeny = "játékos vesztet"
        return eredmeny

    elif osszegzes(gep) > 21:
        eredmeny = "Gép vesztet"
        return eredmeny

#Tesztek


#Megoldás


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
        eredmeny = "Játékos vesztett"
        return eredmeny

    elif osszegzes(gep) > 21:
        eredmeny = "Gép vesztett"
        return eredmeny

#Tesztek
def testek():
    jatekos_vesztett_teszt()
    gep_vesztett_teszt()
    dontetlen_teszt()
def jatekos_vesztett_teszt():
    jatekos = [7, 8, 9]
    gep = [3, 5, 6, 4]
    kapott = eredmény(jatekos, gep)
    vart = "Játékos vesztett"
    if kapott == vart:
        print("Teszt sikeres")
    else:
        print("teszt megbukott")

def gep_vesztett_teszt():
    jatekos = [7, 8, 3]
    gep = [3, 5, 6, 10]
    kapott = eredmény(jatekos, gep)
    vart = "Gép vesztett"
    if kapott == vart:
        print("Teszt sikeres")
    else:
        print("teszt megbukott")


def dontetlen_teszt():
    jatekos = [7, 8, 10]
    gep = [3, 5, 6, 10]
    kapott = eredmény(jatekos, gep)
    vart = "Döntetlen"
    if kapott == vart:
        print("Teszt sikeres")
    else:
        print("teszt megbukott")



testek()
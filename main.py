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
    dontetlen_mindaketten_vesztet_teszt()
    kozelebb21jatekosnyert_teszt()
    kozelebb21gepnyert_teszt()
    dontetlen_eseten_jatekos_nyert_teszt()
    dontetlen_eseten_gep_nyert_teszt()
    dontetlen_eseten_mindaketten_nyert()
def jatekos_vesztett_teszt():
    jatekos = [7, 8, 9]
    gep = [3, 5, 6, 4]
    kapott = eredmény(jatekos, gep)
    vart = "Játékos vesztett"
    print("játékos vesztett")
    if kapott == vart:
        print("Teszt sikeres")
    else:
        print("Teszt megbukott")

def gep_vesztett_teszt():
    jatekos = [7, 8, 3]
    gep = [3, 5, 6, 10]
    kapott = eredmény(jatekos, gep)
    vart = "Gép vesztett"
    print("Gép vesztett")
    if kapott == vart:
        print("Teszt sikeres")
    else:
        print("Teszt megbukott")


def dontetlen_mindaketten_vesztet_teszt():
    jatekos = [7, 8, 10]
    gep = [3, 5, 6, 10]
    kapott = eredmény(jatekos, gep)
    vart = "Döntetlen"
    print("Döntetlen mind a ketten veszített")
    if kapott == vart:
        print("Teszt sikeres")
    else:
        print("teszt megbukott")

def kozelebb21jatekosnyert_teszt():
    jatekos = [7, 8, 5]
    gep = [3, 5, 10]
    kapott = eredmény(jatekos, gep)
    vart = "Játékos nyert"
    print("közelebb 21-hez játekos nyert")
    if kapott == vart:
        print("Teszt sikeres")
    else:
        print("teszt megbukott")

def kozelebb21gepnyert_teszt():
    jatekos = [7, 8, 4]
    gep = [3, 7, 10]
    kapott = eredmény(jatekos, gep)
    vart = "Gép nyert"
    print("közelebb 21-hez gép nyert")
    if kapott == vart:
        print("Teszt sikeres")
    else:
        print("teszt megbukott")

def dontetlen_eseten_jatekos_nyert_teszt():
    jatekos = [7, 8, 4]
    gep = [3, 5, 6, 4]
    kapott = eredmény(jatekos, gep)
    vart = "Játékos nyert"
    print("Döntetlen esetén játékos nyert")
    if kapott == vart:
        print("Teszt sikeres")
    else:
        print("teszt megbukott")

def dontetlen_eseten_gep_nyert_teszt():
    jatekos = [3, 4, 5, 7]
    gep = [7, 8, 4]
    kapott = eredmény(jatekos, gep)
    vart = "Gép nyert"
    print("Döntetlen esetén Gép nyert")
    if kapott == vart:
        print("Teszt sikeres")
    else:
        print("teszt megbukott")

def dontetlen_eseten_mindaketten_nyert():
    jatekos = [3, 7, 10]
    gep = [10, 5, 5]
    kapott = eredmény(jatekos, gep)
    vart = "Gép nyert"
    print("Döntetlen esetén mind a kettő nyert")
    if kapott == vart:
        print("Teszt sikeres")
    else:
        print("teszt megbukott")

testek()
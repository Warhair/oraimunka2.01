'Megoldás'
jatekos = [1,2,3]
gep = [4,5,6,7,7]

def osszegzes(lapok):
    osszeg = 0
    for i in lapok:
        osszeg += i

    return osszeg


def eredmény(jatekos: list, gep: list):
    if osszegzes(jatekos) > 21 and osszegzes(gep) > 21:
        print("Döntetlen")
    elif osszegzes(jatekos) > 21:
        print("játékos vesztet")
    elif osszegzes(gep) > 21:
        print("Gép vesztet")

'Tesztek'


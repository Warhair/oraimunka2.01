'Megoldás'
jatekos = [1,2,3]
gep = [4,5,6,7,7]

def osszegzes(lapok):
    osszeg = 0
    for i in lapok:
        osszeg += i

    return osszeg


def eredmény(jatekos, gep):
    if jatekos > 21 and gep > 21:
        print("Döntetlen")
    elif jatekos > 21:
        print("játékos vesztet")
    elif gep >21:
        print("Gép vesztet")

'Tesztek'
jatekososz = osszegzes(jatekos)
gepo = osszegzes(gep)
eredmény(jatekososz, gepo)
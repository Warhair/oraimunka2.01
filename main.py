'Megoldás'

def eredmény(j_pont, g_pont):
    if j_pont > 21 and g_pont > 21:
        print("Döntetlen")
    elif j_pont > 21:
        print("játékos vesztet")
    elif g_pont >21:
        print("Gép vesztet")

'Tesztek'
from . import affichage
from . import fonction

def avance(lst, tempo, tempo2, dessin, start):
    if (len(fonction.voisin_lab_acc(start[0], lst)) == 2):
        print("start est 1: ", start, "tempo 1:", tempo)
        start = fonction.ancien_voisin(fonction.voisin_lab_acc(start[0], lst), tempo)
        print(start)
    else:
        start = fonction.voisin_lab_acc(start[0], lst)
        dessin = affichage.check(start[0][0], start[0][1], 40)
        affichage.my_carrer(dessin[0], dessin[1], dessin[2], dessin[3], "green")
    print(start)
    return start
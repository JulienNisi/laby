import lib.Labyrinthe
from . import affichage
from . import move

def cordoner (lstlst, n):
    for y in range(len(lstlst)):
        for x in range(len(lstlst[y])):
            if (lstlst[y][x] == n):
                return [y, x]

def entre (lab):
    print("ok")
    return (cordoner(lab, 2))

def sortie (lab):
    if lab == None:
        return
    return(cordoner(lab, 3))

def voisin_lab_acc(couple, lab):
    voisin = []

    if (((lab[couple[0]][couple[1] + 1]) != 0) and ((lab[couple[0]][couple[1] + 1]) != 2)):
        voisin += [[couple[0], couple[1] + 1]]
    if (((lab[couple[0]][couple[1] - 1]) != 0) and ((lab[couple[0]][couple[1] - 1]) != 2)):
        voisin += [[couple[0], couple[1] - 1]]
    if (((lab[couple[0] + 1][couple[1]]) != 0) and ((lab[couple[0] + 1][couple[1]]) != 2)):
        voisin += [[couple[0] + 1, couple[1]]]
    if (((lab[couple[0] - 1][couple[1]]) != 0) and ((lab[couple[0] - 1][couple[1]]) != 2)):
        voisin += [[couple[0] - 1, couple[1]]]

    return (voisin)

def avance(laby, start):
    dessin = []

    if laby[start[0][0]][start[0][1]] != 3:
        laby[start[0][0]][start[0][1]] = 0
    dessin = affichage.check(start[0][0], start[0][1], 40)
    affichage.my_carrer(dessin[0], dessin[1], dessin[2], dessin[3], "blue")

def check(laby, path):
    dessin = []
    tempo = []

    for x in range(len(path) - 1, -1, -1):
        if len(voisin_lab_acc(path[x], laby)) >= 1:
            return [path[x]]
        else:
            tempo = [path[x]]
            dessin = affichage.check(tempo[0][0], tempo[0][1], 40)
            affichage.my_carrer(dessin[0], dessin[1], dessin[2], dessin[3], "#a8c6f0")
            del path[x]
            affichage.lib.graph.refresh()
    return None
"""
def check_win(laby, start):
    if laby[start[0]][start[1]] == 3:
        return True
    else:
        return False
"""
def play_algo(laby):
    start = [entre(laby)]
    path = start
    nb = 0

    while laby[start[0][0]][start[0][1]] != 3:
        if len(voisin_lab_acc(start[0], laby)) == 0:
            start = check(laby, path)
        elif len(voisin_lab_acc(start[0], laby)) == 1:
            start = voisin_lab_acc(start[0], laby)
            path += start
            avance(laby, start)
        else:
            start = voisin_lab_acc(start[0], laby)
            start = [start[0]]
            path += start
            avance(laby, start)
        affichage.lib.graph.refresh()

    return (0)